import csv
import json
import os
import asyncio
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv
from google import genai
from google.genai import types
from discord_client import post_forum_message, tags


# Load environment variables
load_dotenv()

# Configuration
REPO_LIST_FILE = Path("data/repos_list.csv")
KNOWN_RELEASES_FILE = Path("data/known_releases.json")
NIGHTLY_REPORT_FILE = Path("data/nightly_report.md")

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable is not set.")
    exit(1)

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY environment variable is not set.")
    exit(1)

if not DISCORD_WEBHOOK_URL:
    print("Error: DISCORD_WEBHOOK_URL environment variable is not set.")
    exit(1)

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Initialize Gemini Client
ai_client = genai.Client(api_key=GEMINI_API_KEY)


def extract_repo_name(url: str) -> str:
    """Extract the repository owner and name from a GitHub URL or string.

    Args:
        url: The URL or string containing the repository information.

    Returns:
        The owner/repo string.
    """
    prefix = "https://github.com/"
    return url.strip().removesuffix(".git").removeprefix(prefix)


def load_repos() -> list[str]:
    """Load the list of repositories from the CSV file.

    Returns:
        A list of repository names (owner/repo).
    """
    repos = []
    if not REPO_LIST_FILE.exists():
        print(f"Error: {REPO_LIST_FILE} does not exist.")
        exit(1)

    with REPO_LIST_FILE.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and not row[0].startswith("#"):
                repo_name = extract_repo_name(row[0])
                repos.append(repo_name)
    return repos


def load_known_releases() -> dict[str, str]:
    """Load the known releases from the JSON file.

    Returns:
        A dictionary mapping repository names to their latest known release tags.
    """
    if KNOWN_RELEASES_FILE.exists():
        with KNOWN_RELEASES_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_known_releases(data: dict[str, str]) -> None:
    """Save the known releases to the JSON file.

    Args:
        data: A dictionary mapping repository names to release tags.
    """
    KNOWN_RELEASES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with KNOWN_RELEASES_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_report(report_content: str) -> None:
    """Save the nightly report to a markdown file.

    Args:
        report_content: The content of the report.
    """
    NIGHTLY_REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with NIGHTLY_REPORT_FILE.open("w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"Report saved to {NIGHTLY_REPORT_FILE}")


async def get_latest_release(
    client: httpx.AsyncClient, repo: str
) -> dict[str, Any] | None:
    """Fetch the latest release information for a repository from GitHub.

    Args:
        client: The httpx AsyncClient.
        repo: The repository name (owner/repo).

    Returns:
        The release data as a dictionary, or None if the request failed.
    """
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        response = await client.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Warning: No releases found or repo not found for {repo}")
            return None
        else:
            print(f"Error fetching {repo}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception fetching {repo}: {e}")
        return None


async def summarize_release(release: dict[str, Any], repo_name: str) -> str:
    """Generate a summary of the release using Gemini.

    Args:
        release: The release data.
        repo_name: The name of the repository.

    Returns:
        A formatted string summarizing the release.
    """
    tag_name = release.get("tag_name", "Unknown Tag")
    body = release.get("body", "")
    html_url = release.get("html_url", "")

    header = (
        f"**[{repo_name} {tag_name}]({html_url})**"
        if html_url
        else f"**{repo_name}** {tag_name}"
    )

    if not body:
        return f"{header}\n- No release notes provided."

    prompt = f"""
    You are a senior developer advocate. Analyze the provided GitHub release notes.
    
    Repository: {repo_name}
    Tag: {tag_name}
    
    Release Notes:
    {body}

    Extract:
    Summary: A 2-sentence overview of the release.
    Highlights: Top 3 most important features or fixes.
    Breaking Changes: A clear warning if any are present.
    Priority: One of [Breaking, Major, Minor, Bugfix] based on the semantic version and content.
    
    Output must be clean Markdown.
    CRITICAL: The total output MUST be under 1800 characters to fit Discord limits. Be concise.
    At the very end of the response, on a new line, output: "PRIORITY: [Priority]"
    """

    try:
        response = await ai_client.aio.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(include_thoughts=False)
            ),
        )
        return f"{header}\n\n{response.text}\n"
    except Exception as e:
        print(f"Error summarizing {repo_name}: {e}")
        return f"{header}\n- Error generating summary: {e}\nPRIORITY: Bugfix"


async def check_updates() -> None:
    """Check for updates and generate a report."""
    repos = load_repos()
    known_releases = load_known_releases()

    # We still keep track of new releases for the console / local report
    # but the primary delivery mechanism is now Discord.
    new_releases_found = False
    report_entries = []

    print(f"Checking {len(repos)} repositories...")

    async with httpx.AsyncClient() as http_client:
        tasks = []
        tasks.extend(get_latest_release(http_client, repo) for repo in repos)
        results = await asyncio.gather(*tasks)

        for repo, release in zip(repos, results):
            if not release:
                continue

            tag = release.get("tag_name")
            if not isinstance(tag, str):
                continue

            if repo not in known_releases or known_releases[repo] != tag:
                print(f"New release found for {repo}: {tag}")

                # Generate summary
                full_summary = await summarize_release(release, repo)

                # Extract Priority
                priority = "Bugfix"  # Default
                clean_summary = full_summary

                if "PRIORITY: " in full_summary:
                    parts = full_summary.rsplit("PRIORITY: ", 1)
                    clean_summary = parts[0].strip()
                    priority_raw = parts[1].strip()
                    # Clean up priority string
                    priority = priority_raw.split()[0].replace("[", "").replace("]", "")

                # Map to tag
                tag_id = tags.get(priority.lower(), tags["bugfix"])
                applied_tags = [tag_id]

                report_entries.append(clean_summary)

                # Post to Discord
                thread_name = f"{repo} {tag}"
                try:
                    # Truncate to distinct 1990 chars to be safe for Discord's 2000 limit
                    discord_content = (
                        f"{clean_summary[:1990]}..."
                        if len(clean_summary) > 1990
                        else clean_summary
                    )
                    await post_forum_message(
                        http_client,
                        DISCORD_WEBHOOK_URL,
                        thread_name,
                        discord_content,
                        applied_tags,
                    )
                    print(f"Posted to Discord: {thread_name} [Tag: {priority}]")

                    # Update known releases ONLY after successful post
                    known_releases[repo] = tag
                    save_known_releases(known_releases)
                    new_releases_found = True

                except Exception as e:
                    print(f"Failed to post to Discord for {repo}: {e}")
                    # We do NOT update known_releases so we retry next time
            else:
                print(f"No new release for {repo} (Current: {tag})")

    if new_releases_found:
        report_header = "# Nightly GitHub Pulse Report\n\n"
        full_report = report_header + "\n---\n".join(report_entries)
        save_report(full_report)
    else:
        print("\nNo new releases detected.")


if __name__ == "__main__":
    asyncio.run(check_updates())
