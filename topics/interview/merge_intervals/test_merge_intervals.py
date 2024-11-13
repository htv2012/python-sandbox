#!/usr/bin/env python3
import pytest

from merge_intervals import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.merge


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param(
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
            id="example 1",
        ),
        pytest.param([[1, 4], [4, 5]], [[1, 5]], id="example 2"),
        pytest.param([[1, 4], [2, 3]], [[1, 4]], id="tricky"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
