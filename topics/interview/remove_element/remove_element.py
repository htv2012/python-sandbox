#!/usr/bin/env python3
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for element in iter(nums):
            if element != val:
                nums[i] = element
                i += 1
        return i
