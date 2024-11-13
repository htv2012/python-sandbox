#!/usr/bin/env python3
import pytest

from linked_list_cycle import Solution
from list_node import ListNode


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.hasCycle


@pytest.mark.parametrize(
    "array,pos,expected",
    [
        pytest.param([3, 2, 0, -4], 1, True, id="example 1"),
        pytest.param([1, 2], 0, True, id="example 2"),
        pytest.param([1], -1, False, id="example 3"),
        pytest.param([1,2,3], 2, True, id="cycle at last node"),
        pytest.param([], 0, False, id="empty"),
        pytest.param([1], 0, True, id="single node with cycle"),
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

    assert fut(head) == expected
