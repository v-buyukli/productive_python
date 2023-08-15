import pytest

from ..webpage_metrics.webpage import WebPage


@pytest.fixture
def example_webpage():
    return WebPage('https://example.com')


def test_url(example_webpage):
    assert example_webpage.url == 'https://example.com'


def test_download_page(example_webpage):
    example_webpage.download_page()
    assert example_webpage.page is not None


def test_page_size(example_webpage):
    example_webpage.download_page()
    assert example_webpage.page_size == format(len(example_webpage.page), '_')


def test_time_elapsed(example_webpage):
    example_webpage.download_page()
    assert example_webpage.time_elapsed >= 0


def test_tabulate_print(example_webpage, capsys):
    example_webpage.download_page()
    example_webpage.tabulate_print()
    captured = capsys.readouterr()
    assert 'url' in captured.out
    assert 'size(bytes)' in captured.out
    assert 'elapsed(s)' in captured.out
