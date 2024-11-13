#!/usr/bin/env python3
import pytest

from merge_sort_lists import ListNode, Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.mergeTwoLists


def test_example1(fut):
    l1 = ListNode.from_iterable([1, 2, 4])
    l2 = ListNode.from_iterable([1, 3, 4])
    assert list(fut(l1, l2)) == [1, 1, 2, 3, 4, 4]


def test_example2(fut):
    assert fut(None, None) is None


def test_example3(fut):
    actual = fut(None, ListNode.from_iterable([0]))
    assert actual.val == 0
    assert actual.next is None
