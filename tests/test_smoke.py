"""Smoke tests to ensure core helper functions work correctly."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.Helper import get_base_url, get_line_breaker  # noqa: E402


def test_get_base_url():
    assert get_base_url("https://example.com/some/path") == "https://example.com"


def test_get_base_url_with_port():
    assert get_base_url("http://localhost:8080/foo") == "http://localhost:8080"


def test_get_line_breaker():
    result = get_line_breaker()
    assert isinstance(result, str)
    assert len(result) > 0
