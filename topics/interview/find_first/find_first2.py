#!/usr/bin/env python3


def find_first(haystack, needle, index=0) -> int:
    needle_length = len(needle)
    haystack_length = len(haystack)
    if needle_length > haystack_length:
        return -1

    if haystack[:needle_length] == needle:
        return index
    return find_first(haystack[1:], needle, index + 1)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return find_first(haystack, needle, 0)
