import re
from typing import Any

import httpx

tags = {
    "breaking": "1469812659598659816",
    "major": "1469812798006497342",
    "minor": "1469813003003105321",
    "bugfix": "1469813299217432596",
}


async def post_forum_message(
    client: httpx.AsyncClient,
    webhook_url: str,
    thread_name: str,
    content: str,
    applied_tags: list[str] | None = None,
    notify_user_id: str | None = None,
) -> None:
    """Post a message to a Discord Forum channel via webhook.

    Args:
        client: The httpx AsyncClient.
        webhook_url: The Discord webhook URL.
        thread_name: The title of the new thread.
        content: The content of the post (backend-agnostic, no Discord formatting).
        applied_tags: Optional list of tag IDs to apply.
        notify_user_id: Optional Discord user ID to mention at the start of the post.
    """
    # Prepend user mention if requested — Discord-specific, kept out of general content
    discord_content = f"<@{notify_user_id}> {content}" if notify_user_id else content

    payload: dict[str, Any] = {"content": discord_content, "thread_name": thread_name}
    if applied_tags:
        payload["applied_tags"] = applied_tags

    # Resolve any user mentions so they actually ping
    user_ids = re.findall(r"<@(\d+)>", discord_content)
    if user_ids:
        payload["allowed_mentions"] = {"users": user_ids}

    try:
        response = await client.post(webhook_url, json=payload)
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        print(f"Error posting to Discord: {e.response.status_code} - {e.response.text}")
        raise
    except Exception as e:
        print(f"Error posting to Discord: {e}")
        raise
