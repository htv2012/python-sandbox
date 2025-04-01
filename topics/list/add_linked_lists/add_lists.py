#!/usr/bin/env python
"""Adds two lists representing ints"""

from itertools import zip_longest


def add_lists(*args):
    result = list()
    carry = 0
    for terms in zip_longest(*(reversed(li) for li in args), fillvalue=0):
        column_sum = sum(terms) + carry
        carry, column_sum = column_sum // 10, column_sum % 10
        result.insert(0, column_sum)
    if carry:
        result.insert(0, carry)
    return result


if __name__ == "__main__":
    print(add_lists([9, 8, 6], [2, 3, 7, 1]))
    print(add_lists([6, 3, 7], [9, 5], [9, 8, 7, 6]))
