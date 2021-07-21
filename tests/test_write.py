import pytest
from datetime import datetime
from src.edgar_etl import registry
from src.edgar_etl.rss import write


@pytest.fixture
def prefix():
    return registry.rss_prefix()


@pytest.fixture
def test_url():
    return registry.test_url()


def test_write_fn(prefix: str) -> None:
    """Is the filename written correctly?

    Args:
        prefix (str): prefix used to write the filename.
    """
    period = datetime.now()
    target = '-'.join((prefix, str(period.year),
                       str(period.month).zfill(2)))
    target += '.xml'
    # the filename is in the correct format
    assert write.write_fn(period=period) == target
    # the constant in the registry is used at the beginning
    assert write.write_fn(period=period).find(prefix) == 0
