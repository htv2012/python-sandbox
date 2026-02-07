import contextlib
import json

import pytest
import yaml.parser

from json_type.clicklib import json_parse, parse_file

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


USER = {"uid": 501, "alias": "anna"}


@pytest.mark.parametrize(
    "filename, exception, expected",
    [
        # Happy path cases
        pytest.param("valid_no_section.json", None, USER, id="valid json, no section"),
        pytest.param(
            "valid_with_section.json:user1", None, USER, id="valid json, with section"
        ),
        pytest.param("valid_no_section.yaml", None, USER, id="valid yaml, no section"),
        pytest.param(
            "valid_with_section.yaml:user1", None, USER, id="valid yaml, with section"
        ),
        # Error cases
        pytest.param("invalid.json", json.JSONDecodeError, "", id="invalid json"),
        pytest.param("invalid.yaml", yaml.parser.ScannerError, "", id="invalid yaml"),
        pytest.param("filenotfound.yaml", FileNotFoundError, "", id="file not found"),
        pytest.param("unknown_file_type.txt", ValueError, "", id="unknown file type"),
    ],
)
def test_parse_file(data_path, filename, exception, expected):
    filename = f"@{data_path / filename}"
    if exception is not None:
        context = pytest.raises(exception)
    else:
        context = contextlib.nullcontext()

    with context:
        actual = parse_file(filename)
        assert actual == expected
