#!/usr/bin/env python


def unique(lst):
    d = {}
    for i in lst:
        d[i] = 1
    return list(d.keys())


def tryunique(lst):
    print()
    print("Before: ", lst)
    uniq = unique(lst)
    print("After:  ", uniq)


print()
print("TRY UNIQUE")
tryunique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tryunique([1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])
tryunique([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
tryunique([3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
tryunique([])
tryunique([1])
tryunique([1, 1])
