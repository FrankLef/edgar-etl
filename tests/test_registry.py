import pytest
from src.edgar_etl import registry


def test_edgar_url() -> None:
    val = registry.edgar_url()
    assert len(val) != 0, "edgar_url has length 0."


def test_rss_path() -> None:
    val = registry.rss_path()
    assert len(val) != 0, "rss_path has length 0."


def test_rss_file() -> None:
    val = registry.rss_file()
    assert len(val) != 0, "rss_file has length 0."


def test_rss_prefix() -> None:
    val = registry.rss_prefix()
    assert len(val) != 0, "rss_prefix has length 0."
