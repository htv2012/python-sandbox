#!/usr/bin/env python3
from typing import Optional

from linked_list import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        tail = self.swapPairs(head.next.next)
        new_head = head.next
        new_head.next = head
        head.next = tail
        return new_head
