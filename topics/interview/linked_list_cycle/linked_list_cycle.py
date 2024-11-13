#!/usr/bin/env python3
from typing import Optional

from list_node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Corner case
        if head is None or head.next is None:
            return False

        # Create 2 pointers: slow and fast. Fast advances at
        # twice the speed of slow. If there is a cycle,
        # eventually fast will catch up with slow.
        slow = fast = head
        counter = 0

        while fast.next:
            fast = fast.next
            if counter % 2 == 1:
                slow = slow.next
            if fast == slow:
                return True
            counter = counter + 1
        return False
