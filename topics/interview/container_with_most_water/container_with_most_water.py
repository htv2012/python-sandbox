#!/usr/bin/env python3
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0
        left, right = 0, len(height) - 1
        while left < right:
            left_height, right_height = height[left], height[right]
            capacity = (right - left) * min(left_height, right_height)
            if capacity > most:
                most = capacity

            # Move the shorter height. If they are the same, move both ends
            if left_height < right_height:
                left += 1
            elif left_height > right_height:
                right -= 1
            else:
                left += 1
                right -= 1

        return most
