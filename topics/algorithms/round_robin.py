#!/usr/bin/env python3
"""
Implements a round-robin
"""
import itertools


def round_robin(*iterables):
    marker = object()
    queue = itertools.zip_longest(*iterables, fillvalue=marker)
    queue = itertools.chain.from_iterable(queue)
    queue = filter(lambda element: element is not marker, queue)
    yield from queue


def main():
    """Entry"""
    a = [1, 2]
    b = [3, 4, 5]
    c = [6]
    d = [7, 8, 9]

    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    print(f"d={d}")

    print("-" * 20)
    print(f"round robin of a, b, c, d: {list(round_robin(a, b, c, d))}")


if __name__ == "__main__":
    main()
