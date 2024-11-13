#!/usr/bin/env python3
from typing import Optional

from list_node import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_hare = p_tortoise = head
        counter = 0

        while p_hare and p_hare.next:
            # Advance the hare and check
            p_hare = p_hare.next
            if p_hare is p_tortoise:
                return p_hare

            # Advance the tortoise and check
            if counter % 2 == 1:
                p_tortoise = p_tortoise.next
            if p_hare is p_tortoise:
                return p_hare

            # Advance the counter, use to count steps:
            # hare runs twice as fast as tortoise
            counter += 1

        # Exiting the while loop means there is no cycle
        return None
