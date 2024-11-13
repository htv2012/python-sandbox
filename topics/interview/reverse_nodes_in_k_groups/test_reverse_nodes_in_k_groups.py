#!/usr/bin/env python3
import pytest

from reverse_nodes_in_k_groups import ListNode, Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.reverseKGroup


@pytest.mark.parametrize(
    "head,k,expected",
    [
        pytest.param(None, 2, [], id="None, k=2"),
        pytest.param([1], 2, [1], id="single item, k=2"),
        pytest.param([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4], id="no remainder"),
        pytest.param([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5], id="example 1"),
        pytest.param([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5], id="example 2"),
        pytest.param([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5], id="k=1"),
    ],
)
def test_reverse(fut, head, k, expected):
    if head is not None:
        head = ListNode.from_iterable(head)

    print(f"{head=}, {k=}")
    new_head = fut(head, k)
    print(f"{new_head=}")

    node = new_head
    for expected_value in expected:
        assert node.val == expected_value
        node = node.next
    assert node is None
