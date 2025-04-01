#!/usr/bin/env python3
"""
Given a linked list:
    1 -> 2 -> 3 -> 4 -> 5 -> 8 -> 13 -> 21 -> 6
Re-order by taking turn taking an element from the left, then from the right
and work your way inside the list, the resulting list is:
    1 -> 6 -> 2 -> 21 -> 3 -> 13 -> 4 -> 8

- The list is not ordered in any way
- The kind of data is irrelevant
"""


# ======================================================================
# Implementation
# ======================================================================
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __iter__(self):
        current = self
        while current is not None:
            yield current.data
            current = current.next

    @classmethod
    def from_iter(cls, seq):
        head = None
        tail = None
        for data in seq:
            node = cls(data)
            if head is None:
                head = node
            if tail is not None:
                tail.next = node
            tail = node
        return head


def reverse_list(llist):
    head = llist
    prev = None
    current = llist
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


# ======================================================================
# Test
# ======================================================================


def test_node():
    node = Node(5)
    assert node.data == 5
    assert node.next is None


def test_iter():
    n3 = Node(7)
    n2 = Node(19, n3)
    n1 = Node(8, n2)
    actual = list(n1)
    assert actual == [8, 19, 7]


def test_from_iter():
    original = [3, 8, 94, 25, 7, 10, 8]
    llist = Node.from_iter(original)
    assert list(llist) == original


def test_reverse_normal():
    original = [1, 3, 2, 6, 10, 19, 8, 7]
    llist = Node.from_iter(original)
    llist = reverse_list(llist)
    assert list(llist) == [7, 8, 19, 10, 6, 2, 3, 1]
