#!/usr/bin/env python3
from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        buckets = []
        letters = ""
        for digit in digits:
            if digit == "2":
                letters = "abc"
            elif digit == "3":
                letters = "def"
            elif digit == "4":
                letters = "ghi"
            elif digit == "5":
                letters = "jkl"
            elif digit == "6":
                letters = "nmo"
            elif digit == "7":
                letters = "pqrs"
            elif digit == "8":
                letters = "tuv"
            elif digit == "9":
                letters = "wxyz"
            buckets.append(letters)
        out = ["".join(x) for x in product(*buckets)]
        return out
