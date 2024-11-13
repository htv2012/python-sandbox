#!/usr/bin/env python3
import pytest

from find_in_rotated import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.search


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        pytest.param([4, 5, 6, 7, 0, 1, 2], 0, 4, id="example 1"),
        pytest.param([4, 5, 6, 7, 0, 1, 2], 3, -1, id="example 2"),
        pytest.param([1], 0, -1, id="example3"),
        pytest.param([1, 2, 4, 5, 6, 7], 3, -1, id="not found"),
    ],
)
def test_solution(fut, nums, target, expected):
    assert fut(nums, target) == expected
