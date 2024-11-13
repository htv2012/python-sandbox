#!/usr/bin/env python3
import pytest

from linked_list import from_iterable
from solution import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.swapPairs


def test_solution_example2(fut):
    assert fut(None) is None


def test_solution_example3(fut):
    head = from_iterable([1])
    assert head.val == 1
    assert head.next is None
    out = fut(head)
    assert out is head
    assert out.val == 1
    assert out.next is None


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param([1, 2, 3, 4], [2, 1, 4, 3], id="example 1"),
        pytest.param([1, 2, 3], [2, 1, 3], id="odd number of nodes"),
    ],
)
def test_solution(fut, indata, expected):
    head = from_iterable(indata)
    second = head.next
    out = fut(head)
    assert out is second
