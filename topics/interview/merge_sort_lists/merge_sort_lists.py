#!/usr/bin/env python3
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        node = self
        while node:
            values.append(node.val)
            node = node.next
        return f"<ListNode count={len(values)}, nodes={values}>"

    def __iter__(self):
        node = self
        while node is not None:
            yield node.val
            node = node.next

    @classmethod
    def from_iterable(cls, it):
        root = None
        prev = None
        node = None
        for value in it:
            node = cls(value)
            if prev is None:
                root = node
            else:
                prev.next = node
            prev = node
        return root


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = None
        node = None
        prev = None
        while list1 and list2:
            if list1.val < list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            if prev is not None:
                prev.next = node
            else:
                root = node
            prev = node

        remainder = list1 or list2
        while remainder:
            node = ListNode(remainder.val)
            if prev is not None:
                prev.next = node
            else:
                root = node
            prev = node
            remainder = remainder.next

        return root
