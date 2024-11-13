#!/usr/bin/env python

"""
Demo: takewhile swallows up an element
"""

import itertools

if __name__ == "__main__":
    items = list(range(10))
    it = iter(items)

    print("Takewhile swallows an element in the sequence:")
    print("Original:      ", items)
    print("Take while < 4:", list(itertools.takewhile(lambda x: x < 4, it)))
    print("Remainder:     ", list(it))  # 4 got swallowed

    it = iter(items)
    print("\nDropwhile does not:")
    print("Original:      ", items)
    print("Drop while < 4:", list(itertools.dropwhile(lambda x: x < 4, it)))
