"""Tests for rate limiting in release summarization."""

from typing import Any

import pytest
from pytest_mock import MockerFixture

from github_news.check_releases import summarize_release


@pytest.mark.asyncio
async def test_summarize_release_rate_limit_fix(mocker: MockerFixture) -> None:
    """Verify that summarize_release retries on 429 errors."""
    # Mock the ai_client and its nested structures
    mock_ai_client = mocker.patch("github_news.check_releases.ai_client")

    # We need to mock ai_client.aio.models.generate_content
    mock_generate_content = mocker.AsyncMock()
    mock_ai_client.aio.models.generate_content = mock_generate_content

    # Simulate a 429 error followed by a success
    error_message = "429 RESOURCE_EXHAUSTED"
    mock_generate_content.side_effect = [
        Exception(error_message),
        mocker.MagicMock(text="Successful summary"),
    ]

    # Mock asyncio.sleep to avoid waiting in tests
    # Tenacity uses asyncio.sleep for async retrying
    mocker.patch("asyncio.sleep", mocker.AsyncMock())

    release = {
        "tag_name": "v1.0.0",
        "body": "Some release notes",
        "html_url": "http://example.com",
    }
    repo_name = "test/repo"

    result = await summarize_release(release, repo_name)

    # Now it should succeed
    assert "Successful summary" in result
    assert "Error generating summary" not in result
    # Verify it was called twice
    assert mock_generate_content.call_count == 2


@pytest.mark.asyncio
async def test_summarize_release_other_error_no_retry(mocker: MockerFixture) -> None:
    """Verify that summarize_release does not retry on other errors."""
    # Mock the ai_client
    mock_ai_client = mocker.patch("github_news.check_releases.ai_client")
    mock_generate_content = mocker.AsyncMock()
    mock_ai_client.aio.models.generate_content = mock_generate_content

    # Simulate a 400 error (not 429)
    error_message = "400 BAD_REQUEST"
    mock_generate_content.side_effect = Exception(error_message)

    release: dict[str, Any] = {"tag_name": "v1.0.0", "body": "Some release notes"}
    repo_name = "test/repo"

    result = await summarize_release(release, repo_name)

    # It should fail immediately without retry
    assert "Error generating summary" in result
    assert error_message in result
    assert mock_generate_content.call_count == 1
