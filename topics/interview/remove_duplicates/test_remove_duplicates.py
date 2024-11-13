#!/usr/bin/env python3
import pytest

from solution import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.removeDuplicates


@pytest.mark.parametrize(
    "array,expected_count,expected_array",
    [
        pytest.param([1, 1, 2], 2, [1, 2], id="example 1"),
        pytest.param(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4], id="example 2"
        ),
        pytest.param([1, 1, 1, 1], 1, [1], id="same element"),
        pytest.param([1, 2, 3, 4], 4, [1, 2, 3, 4], id="all unique"),
    ],
)
def test_solution(fut, array, expected_count, expected_array):
    actual_count = fut(array)
    assert actual_count == expected_count
    assert array[:actual_count] == expected_array
