import json
import pathlib
import types

import pytest

from leet.parse import parse_test_cases

ARTIFACTS_DIR = pathlib.Path(__file__).parent / "artifacts"
assert ARTIFACTS_DIR.is_dir()


def get_content(filename: str):
    path = ARTIFACTS_DIR / filename
    return path.read_text()


def get_test_cases(filename: str):
    path = ARTIFACTS_DIR / filename
    with open(path) as stream:
        test_cases = json.load(stream)
    return test_cases


def create_param(num: int):
    num = f"{num:04}"
    content = get_content(f"content_{num}.txt")
    test_cases = get_test_cases(f"test_cases_{num}.json")
    return pytest.param(
        types.SimpleNamespace(content=content, test_cases=test_cases),
        id=f"leetcode {num}",
    )


@pytest.mark.parametrize(
    "test_case",
    [
        create_param(344),
        create_param(349),
        create_param(367),
        create_param(374),
    ],
)
def test_parse_test_cases(test_case):
    actual = parse_test_cases(test_case.content)
    assert actual == test_case.test_cases
