#!/usr/bin/env python3
import pytest

from container_with_most_water import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.maxArea


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, id="example 1"),
        pytest.param([1, 1], 1, id="example2"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
