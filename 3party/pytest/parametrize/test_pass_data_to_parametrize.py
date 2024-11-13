"""
Passing parameters to parametrize.

https://docs.pytest.org/en/latest/how-to/fixtures.html#parametrizing-fixtures
https://docs.pytest.org/en/latest/reference/reference.html#pytest-fixture
"""

import logging
import urllib.parse

import pytest


@pytest.fixture(
    params=[
        pytest.param(("http", 80), id="insecured"),
        pytest.param(("https", 443), id="secured"),
    ],
)
def url(request):
    proto, port = request.param
    url_value = urllib.parse.urlunparse((proto, f"host.com:{port}", "", "", "", ""))
    return url_value


def test_url(url):
    logging.debug("url=%r", url)
    assert url in {"http://host.com:80", "https://host.com:443"}
