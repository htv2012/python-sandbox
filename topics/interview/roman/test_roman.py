#!/usr/bin/env python3
import pytest

from solution import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.intToRoman


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param(3, "III", id="example 1"),
        pytest.param(58, "LVIII", id="example 2"),
        pytest.param(1994, "MCMXCIV", id="example 3"),
        pytest.param(1, "I", id="lower edge"),
        pytest.param(3999, "MMMCMXCIX", id="upper edge"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
