#!/usr/bin/env python3
import pytest

from add_binary import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.addBinary


@pytest.mark.parametrize(
    "a,b,expected",
    [
        pytest.param("11", "1", "100", id="example 1"),
        pytest.param("1010", "1011", "10101", id="example 2"),
        pytest.param("0", "1", "1", id="0 and 1"),
    ],
)
def test_solution(fut, a, b, expected):
    assert fut(a, b) == expected
