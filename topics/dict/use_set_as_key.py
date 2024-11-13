#!/usr/bin/env python3
"""Use a set as key to a dictionary.

A set cannot be a key, but a frozen set can. So we can use a frozen
set instead.
"""


def main():
    """Entry"""
    print("\n# Attempt to use sets as key")
    set1 = set("abc")
    set2 = set("def")

    try:
        dict_object = {set1: 1, set2: 2}
    except TypeError as error:
        print("Error:", error)

    print("\n# Use frozen sets as key")
    frozen_set1 = frozenset("abc")
    frozen_set2 = frozenset("def")

    dict_object = {frozen_set1: 1, frozen_set2: 2}
    print("dict_object =", dict_object)


if __name__ == "__main__":
    main()
