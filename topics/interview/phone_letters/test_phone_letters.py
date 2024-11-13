#!/usr/bin/env python3
import pytest

from solution import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.letterCombinations


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param(
            "23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], id="example 1"
        ),
        pytest.param("", [], id="example 2"),
        pytest.param("2", ["a", "b", "c"], id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
