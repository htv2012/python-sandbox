#!/usr/bin/env python3
import pytest

from solution import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.longestCommonPrefix


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param(["flower", "flow", "flight"], "fl", id="example 1"),
        pytest.param(["dog", "racecar", "car"], "", id="example 2"),
        pytest.param(
            ["interface", "international", "interactive", "internship"],
            "inter",
            id="extra 1",
        ),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
