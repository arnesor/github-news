"""Pytest configuration and shared fixtures."""

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Register custom markers."""
    config.addinivalue_line(
        "markers",
        "integration: marks tests that make real network calls (deselect with '-m not integration')",
    )
