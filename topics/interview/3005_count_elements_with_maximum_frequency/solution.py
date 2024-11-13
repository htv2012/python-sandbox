from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        highest_frequency_so_far = 0
        frequency = {}
        for number in nums:
            new_count = frequency.setdefault(number, 0) + 1
            frequency[number] = new_count
            if highest_frequency_so_far < new_count:
                highest_frequency_so_far = new_count

        result = sum(
            count for count in frequency.values() if count == highest_frequency_so_far
        )
        return result
