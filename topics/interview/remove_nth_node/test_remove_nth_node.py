#!/usr/bin/env python3
import pytest

from remove_nth_node import ListNode, Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.removeNthFromEnd


@pytest.mark.parametrize(
    "array,n,expected",
    [
        pytest.param([1, 2, 3, 4, 5], 2, [1, 2, 3, 5], id="example 1"),
        pytest.param([1], 1, [], id="example 2"),
        pytest.param([1, 2], 1, [1], id="example 3"),
        pytest.param([1, 2, 3, 4], 4, [2, 3, 4], id="remove head"),
    ],
)
def test_solution(fut, array, n, expected):
    head = ListNode.from_iterable(array)
    actual = fut(head, n)
    node = actual
    for expected_value in expected:
        assert node.val == expected_value
        node = node.next
    assert node is None
