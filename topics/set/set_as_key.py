#!/usr/bin/env python3
"""Can we use frozenset as key in dictionary."""


def main():
    """Entry"""
    dict_object = {
        frozenset([1, 2, 3]): True,
        frozenset({1, 2}): True,
    }
    print(dict_object)


if __name__ == "__main__":
    main()
