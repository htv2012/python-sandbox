#!/usr/bin/env python3
import pytest

from solution import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.isValid


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param("()", True, id="example 1"),
        pytest.param("()[]{}", True, id="example 2"),
        pytest.param("(]", False, id="example 2"),
        pytest.param("(", False, id="missing right"),
        pytest.param(")", False, id="missing left"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) is expected
