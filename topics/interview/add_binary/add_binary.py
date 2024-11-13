#!/usr/bin/env python3
import collections
import itertools


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        out = collections.deque()

        for x, y in itertools.zip_longest(a, b, fillvalue="0"):
            carry, sum_ = divmod(int(x) + int(y) + carry, 2)
            out.appendleft(str(sum_))

        if carry:
            out.appendleft(str(carry))

        result = "".join(out)
        return result
