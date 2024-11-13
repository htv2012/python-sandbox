#!/usr/bin/env python

from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    items = list(range(5))
    for pair in pairwise(items):
        print(pair)


if __name__ == "__main__":
    main()
