"""Mocked unit tests for discord_client.post_forum_message."""

from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from github_news.discord_client import post_forum_message


@pytest.fixture
def mock_client(mocker: MockerFixture) -> MagicMock:
    """Return a mock httpx.AsyncClient with a post method that succeeds by default."""
    client = mocker.MagicMock()
    response = mocker.MagicMock()
    response.raise_for_status = mocker.MagicMock()
    client.post = mocker.AsyncMock(return_value=response)
    return client


async def test_basic_post(mock_client: MagicMock) -> None:
    """A plain post sends content and thread_name without allowed_mentions."""
    await post_forum_message(
        mock_client, "https://example.com/webhook", "My Thread", "Hello!"
    )

    mock_client.post.assert_called_once()
    _, kwargs = mock_client.post.call_args
    payload = kwargs["json"]
    assert payload["content"] == "Hello!"
    assert payload["thread_name"] == "My Thread"
    assert "allowed_mentions" not in payload


async def test_applied_tags_included(mock_client: MagicMock) -> None:
    """applied_tags are forwarded to the payload."""
    await post_forum_message(
        mock_client,
        "https://example.com/webhook",
        "Thread",
        "Content",
        applied_tags=["tag1"],
    )

    _, kwargs = mock_client.post.call_args
    assert kwargs["json"]["applied_tags"] == ["tag1"]


async def test_notify_user_id_prepends_mention(mock_client: MagicMock) -> None:
    """When notify_user_id is set, the mention is prepended and allowed_mentions is set."""
    await post_forum_message(
        mock_client,
        "https://example.com/webhook",
        "Release Thread",
        "New release!",
        notify_user_id="123456789",
    )

    _, kwargs = mock_client.post.call_args
    payload = kwargs["json"]
    assert payload["content"] == "<@123456789> New release!"
    assert payload["allowed_mentions"] == {"users": ["123456789"]}


async def test_notify_user_id_none_no_mention(mock_client: MagicMock) -> None:
    """When notify_user_id is None, no mention is added and allowed_mentions is absent."""
    await post_forum_message(
        mock_client,
        "https://example.com/webhook",
        "Bugfix Thread",
        "Small fix.",
        notify_user_id=None,
    )

    _, kwargs = mock_client.post.call_args
    payload = kwargs["json"]
    assert payload["content"] == "Small fix."
    assert "allowed_mentions" not in payload


async def test_http_error_is_re_raised(
    mock_client: MagicMock, mocker: MockerFixture
) -> None:
    """HTTPStatusError from raise_for_status propagates to the caller."""
    import httpx

    mock_response = mocker.MagicMock()
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "403",
        request=mocker.MagicMock(),
        response=mocker.MagicMock(status_code=403, text="Forbidden"),
    )
    mock_client.post = mocker.AsyncMock(return_value=mock_response)

    with pytest.raises(httpx.HTTPStatusError):
        await post_forum_message(mock_client, "https://example.com/webhook", "T", "C")


async def test_webhook_url_used_as_is(mock_client: MagicMock) -> None:
    """The webhook URL is passed directly to client.post."""
    url = "https://discord.com/api/webhooks/1234/secret"
    await post_forum_message(mock_client, url, "Thread", "Content")

    args, _ = mock_client.post.call_args
    assert args[0] == url
