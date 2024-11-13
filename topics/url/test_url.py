#!/usr/bin/env python3
import pytest

from url import Url


@pytest.fixture
def root():
    return Url("https://example.com")


def test_str(root):
    assert str(root) == "https://example.com"


def test_join_expect_str(root):
    assert root / "/api/help" == "https://example.com/api/help"


def test_join_expect_obj(root):
    ep = root // "api"
    assert isinstance(ep, Url)
    assert str(ep) == "https://example.com/api"


def test_double_join(root):
    ep = root // "api" / "v1"
    assert ep == "https://example.com/api/v1"


@pytest.mark.parametrize(
    "args,kwargs,expected",
    [
        pytest.param(tuple(), None, "https://example.com", id="no args, no kwargs"),
        pytest.param(("api", "v1"), {}, "https://example.com/api/v1", id="args only"),
        pytest.param(
            ("api", "v1", "get?"),
            {"name": "John Doe", "age": 29},
            "https://example.com/api/v1/get?name=John+Doe&age=29",
            id="with kwargs",
        ),
    ],
)
def test_call(root, args, kwargs, expected):
    if kwargs is None:
        assert root(*args) == expected
    else:
        assert root(*args, **kwargs) == expected
