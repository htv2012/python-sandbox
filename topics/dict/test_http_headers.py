import pytest
from http_headers import Headers


@pytest.fixture
def headers():
    return Headers(
        {
            "content-type": "application/json",
        }
    )


def test_key_cases(headers):
    assert headers["content-type"] == "application/json"
    assert headers["CONTENT-TYPE"] == "application/json"
    assert headers["Content-Type"] == "application/json"


def test_add():
    headers = Headers()
    headers["keep-alive"] = "timeout=5, max=1000"
    assert headers["keep-alive"] == "timeout=5, max=1000"
    assert headers["KEEP-ALIVE"] == "timeout=5, max=1000"
    assert headers["Keep-Alive"] == "timeout=5, max=1000"


def test_update():
    headers = Headers(
        {
            "content-type": "application/json",
        }
    )
    headers.update({"keep-alive": "timeout=5, max=1000"})

    assert headers["keep-alive"] == "timeout=5, max=1000"
    assert headers["KEEP-ALIVE"] == "timeout=5, max=1000"
    assert headers["Keep-Alive"] == "timeout=5, max=1000"


def test_conversion(headers):
    assert headers == {"Content-Type": "application/json"}
