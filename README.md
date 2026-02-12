# GitHub News Monitor

`github-news` is an automated utility to monitor GitHub repositories for new releases, generate AI-powered summaries using Google Gemini, and deliver reports directly to a Discord Forum.

## Features

- **Automated Monitoring:** Regularly checks a list of GitHub repositories for new releases.
- **AI Summarization:** Uses Google Gemini (`gemini-flash-latest`) to summarize release notes, highlighting key features and breaking changes.
- **Smart Categorization:** Automatically assigns priorities (Breaking, Major, Minor, Bugfix) based on release content.
- **Discord Integration:** Posts summaries to a Discord Forum channel with appropriate tags.
- **Local Reporting:** Generates a `latest_report.md` file and maintains a `known_releases.json` state.

## Prerequisites

- **Python:** 3.13 or higher.
- **Package Manager:** [uv](https://github.com/astral-sh/uv) is required for dependency management and execution.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/github-news.git
   cd github-news
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

## Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
GITHUB_TOKEN=your_github_personal_access_token
GEMINI_API_KEY=your_google_gemini_api_key
DISCORD_WEBHOOK_URL=your_discord_forum_webhook_url
```

- `GITHUB_TOKEN`: Required to access the GitHub API and avoid rate limits.
- `GEMINI_API_KEY`: Required for AI-powered summarization.
- `DISCORD_WEBHOOK_URL`: Required to post updates to Discord.

### Repository List

Add the GitHub repository URLs you want to monitor to `data/repos_list.csv`. One URL per line.

```csv
https://github.com/astral-sh/uv
https://github.com/psf/black
```

## Usage

Run the monitor manually using `uv`:

```bash
uv run github-news
```

Alternatively, you can run the script directly:

```bash
uv run src/github_news/main.py
```

## Automation

This project includes a GitHub Action workflow located in `.github/workflows/check_releases.yml` that runs the monitor daily at midnight UTC.

To use the workflow, ensure you have added the following secrets to your GitHub repository:
- `GEMINI_API_KEY`
- `DISCORD_WEBHOOK_URL`

The workflow automatically manages the state by committing changes to a `data` branch.

## Development

### Coding Standards

- **Type Hinting:** Uses modern PEP 585 and PEP 604 syntax (e.g., `list[str]`, `str | None`).
- **Asynchronous I/O:** Built with `asyncio` and `httpx`.
- **Linting & Formatting:** Managed by `ruff`.
- **Type Checking:** Managed by `mypy`.

### Commands

- **Run Tests:** `uv run pytest`
- **Lint Code:** `uv run ruff check .`
- **Format Code:** `uv run ruff format .`
- **Type Check:** `uv run mypy .`

## Documentation

Code follows the **Google Python Style Guide**. Every function, class, and module includes detailed docstrings with `Args` and `Returns` sections.
