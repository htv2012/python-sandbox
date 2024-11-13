#!/usr/bin/env python3
import itertools


def find_first(haystack, needle, index=0) -> int:
    for h, n in itertools.zip_longest(haystack, needle, fillvalue=None):
        if n is None:
            return index
        elif h is None:
            return -1
        elif h != n:
            return find_first(haystack=haystack[1:], needle=needle, index=index + 1)
    return index


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return find_first(haystack, needle, 0)
