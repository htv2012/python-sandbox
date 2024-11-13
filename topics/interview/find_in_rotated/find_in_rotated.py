#!/usr/bin/env python3
from typing import List


def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    array_size = len(nums)
    if array_size == 0:
        return -1

    index = 0
    count = 0
    while True:
        prev = nums[index]

        if target <= nums[index]:
            index = (index - 1) % array_size
        else:
            index = (index + 1) % array_size

        current = nums[index]
        if target == current:
            return index

        if (prev < target < current) or (prev > target > current):
            return -1

        count += 1
        if count >= array_size:
            return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return search_in_rotated_sorted_array(nums, target)
