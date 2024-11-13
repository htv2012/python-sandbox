#!/usr/bin/env python3
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {"": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        out = 0
        prev = ""
        for ch in s:
            if table[prev] < table[ch]:
                out = out - table[prev]
                out += table[ch] - table[prev]
            else:
                out += table[ch]
            prev = ch
        return out
