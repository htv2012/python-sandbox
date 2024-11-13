#!/usr/bin/env python3
from typing import List, Optional

from list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pre_head = ListNode(0)
        tail = pre_head
        lists = [node for node in lists if node is not None]
        while lists:
            buckets = lists
            lists = []
            smallest = min(node.val for node in buckets if node is not None)
            for node in buckets:
                if node is not None and node.val == smallest:
                    tail.next = node
                    node = node.next
                    tail = tail.next
                    tail.next = None
                if node is not None:
                    lists.append(node)
        return pre_head.next
