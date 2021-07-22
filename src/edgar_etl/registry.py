"""Singleton with the EDGAR specs such as url and prefix"""

# The public example provided by IANA
EXAMPLE_URL = 'http://example.com'
# A simple HTTP request and response service by Kenneth Reitz
SIMPLE_URL = 'https://httpbin.org'


EDGAR_URL = 'https://www.sec.gov/Archives/edgar'
EDGAR_URL_MONTH = 'https://www.sec.gov/Archives/edgar/monthly'
# this is the olf edgar monthly url.  It has http instead of https
# it is useful to test, for example, the http code 301
EDGAR_URL_MONTH_OLD = 'http://www.sec.gov/Archives/edgar/monthly'
EDGAR_XBRLRSS = 'xbrlrss'

RSS_2020_PATH = r'C:\Users\Public\MyPy\data\edgar\xbrlrss\2020'
RSS_202001_FILE = 'xbrlrss-2020-01.xml'
RSS_2021_PATH = r'C:\Users\Public\MyPy\data\edgar\xbrlrss\2021'
RSS_202101_FILE = 'xbrlrss-2021-01.xml'


def edgar_url(choice: int = 0) -> str:
    val = (EDGAR_URL, EDGAR_URL_MONTH, EDGAR_URL_MONTH_OLD)
    return val[choice]


def rss_path(choice: int = 0) -> str:
    val = (RSS_2020_PATH, RSS_2021_PATH)
    return(val[choice])


def rss_file(choice: int = 0) -> str:
    val = (RSS_202001_FILE, RSS_202101_FILE)
    return(val[choice])


def rss_prefix(choice: int = 0) -> str:
    """The prefix used to create te rss feed file.

    Args:
        choice (int, optional): Choice of prefix for rss file. Defaults to 0.

    Returns:
        str: Prefix used to create te rss feed file.
    """
    val = (EDGAR_XBRLRSS,)
    return(val[choice])
