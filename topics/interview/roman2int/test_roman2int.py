#!/usr/bin/env python3
import pytest

from solution import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.romanToInt


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param("III", 3, id="example 1"),
        pytest.param("LVIII", 58, id="example 2"),
        pytest.param("MCMXCIV", 1994, id="example 3"),
        pytest.param("IV", 4, id="four"),
        pytest.param("MMMCMXCIX", 3999, id="3999"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
