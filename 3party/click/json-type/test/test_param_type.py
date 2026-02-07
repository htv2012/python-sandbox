import pytest

from json_type.clicklib import json_parse

from .sample import SampleEnum, User


@pytest.mark.parametrize(
    "json_str, expected",
    [
        pytest.param("9", 9, id="int"),
        pytest.param("hello", "hello", id="fallback"),
        pytest.param('"hello"', "hello", id="str"),
        pytest.param('{"name": "Anna"}', {"name": "Anna"}, id="dict"),
        pytest.param("[1, 2]", [1, 2], id="list"),
    ],
)
def test_json_parse(json_str, expected):
    assert json_parse(json_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        pytest.param("one", SampleEnum.ONE, id="happy path"),
        pytest.param("One", SampleEnum.ONE, id="case insensitive"),
    ],
)
def test_convert_enum(convert_enum, input_str, expected):
    assert convert_enum(input_str, None, None) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        pytest.param(
            '{"uid": 501, "alias": "anna"}', User(501, "anna"), id="happy path"
        ),
        pytest.param(
            '{"uid": 501, "alias": "anna", "is_admin": true}',
            User(501, "anna", True),
            id="all params specified",
        ),
    ],
)
def test_convert_simple(convert_user, input_str, expected):
    assert convert_user(input_str, None, None) == expected
