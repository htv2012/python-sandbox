#!/usr/bin/env python3
import pytest

from remove_element import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.removeElement


@pytest.mark.parametrize(
    "array,val,expected_count,expected_array",
    [
        pytest.param([3, 2, 2, 3], 3, 2, [2, 2], id="example 1"),
        pytest.param([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4], id="example 2"),
        pytest.param([], 9, 0, [], id="empty array"),
        pytest.param([1, 1, 1, 1, 1], 1, 0, [], id="remove all"),
        pytest.param([1, 2, 3, 4], 5, 4, [1, 2, 3, 4], id="remove none"),
    ],
)
def test_remove_element(fut, array, val, expected_count, expected_array):
    assert fut(array, val) == expected_count
    for i in range(expected_count):
        assert array[i] == expected_array[i]
