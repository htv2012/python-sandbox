#!/usr/bin/env python3
import pytest
from list_node import ListNode, assert_values

from merge_k_sorted_lists import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.mergeKLists


@pytest.mark.parametrize(
    "lists,expected",
    [
        pytest.param(
            [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6], id="example 1"
        ),
        pytest.param([], [], id="example 2"),
        pytest.param([[]], [], id="example 3"),
    ],
)
def test_merge_k_sorted_lists(fut, lists, expected):
    if lists is not None:
        lists = [ListNode.from_iterable(li) for li in lists]
    actual = fut(lists)
    assert_values(actual, expected)
