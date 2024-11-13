#!/usr/bin/env python3
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        it = iter(intervals)
        out = [next(it)]
        for a, b in it:
            last = out[-1][-1]
            if a <= last:
                out[-1][-1] = max(b, last)
            else:
                out.append([a, b])
        return out
