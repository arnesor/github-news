"""Integration test: sends a real message to the Discord forum via webhook.

Run explicitly with:
    uv run pytest -m integration tests/test_discord_mention.py

This test is excluded from normal pytest runs (see pyproject.toml addopts).
"""

import os

import httpx
import pytest
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
ARNESO_USER_ID = "866617779650035732"


@pytest.mark.integration
async def test_user_mention_creates_thread_and_pings() -> None:
    """Post a real message to Discord and verify the request succeeds."""
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{WEBHOOK_URL}?wait=true",
            json={
                "thread_name": "Integration mention test",
                "content": f"<@{ARNESO_USER_ID}> integration test ping",
                "allowed_mentions": {"users": [ARNESO_USER_ID]},
            },
        )
        assert r.status_code == 200, f"Unexpected status: {r.status_code} — {r.text}"
        data = r.json()
        assert data["channel_id"], "Expected a thread channel_id in the response"
