#!/usr/bin/env python3
import pytest

from linked_list_cycle2 import Solution
from list_node import ListNode


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.detectCycle


@pytest.mark.parametrize(
    "array,pos,expected",
    [
        pytest.param([3, 2, 0, -4], 1, 2, id="example 1"),
        pytest.param([1, 2], 0, 1, id="example 2"),
        pytest.param([1], -1, None, id="example 3"),
        pytest.param([1, 2, 3], 2, 3, id="cycle at last node"),
        pytest.param([], 0, None, id="empty"),
        pytest.param([1], 0, 1, id="single node with cycle"),
    ],
)
def test_solution(fut, array, pos, expected):
    head = ListNode.from_iterable(array)
    # Create a cycle
    if pos != -1 and head is not None:
        target = head
        for _ in range(pos):
            target = target.next
        last = target
        while last.next:
            last = last.next
        last.next = target

    actual = fut(head)
    if expected is None:
        assert actual is None
    else:
        assert expected == actual.val
