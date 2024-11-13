#!/usr/bin/env python3
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        it = iter(nums)
        next(it)
        for element in it:
            if nums[i] != element:
                i += 1
                nums[i] = element
        return i + 1
