#!/usr/bin/env python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Traverse from the right to left, skip spaces
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1

        # Traverse from right to left, count the non spaces
        count = 0
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
        return count
