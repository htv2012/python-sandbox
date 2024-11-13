#!/usr/bin/env python3
import pytest

from rotate_list import ListNode, Solution, from_iterable


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.rotateRight


def assert_values(head: ListNode, expected: list):
    node = head
    for expected_value in expected:
        assert node.val == expected_value
        node = node.next
    assert node is None


@pytest.mark.parametrize(
    "head,k,expected",
    [
        pytest.param([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3], id="example 1"),
        pytest.param([0, 1, 2], 4, [2, 0, 1], id="example 2"),
        pytest.param([], 5, [], id="empty list"),
        pytest.param([1], 5, [1], id="single-item list"),
        pytest.param([1, 2, 3], 3, [1, 2, 3], id="full rotation"),
        pytest.param([1, 2], 5, [2, 1], id="short list"),
        pytest.param([1, 2], 0, [1, 2], id="k is 0"),
        pytest.param(
            [1, 2, 3, 4, 5], 10, [1, 2, 3, 4, 5], id="k is multiple of list length"
        ),
    ],
)
def test_rotate_list(fut, head, k, expected):
    head = from_iterable(head)
    new_head = fut(head, k)
    assert_values(new_head, expected)
