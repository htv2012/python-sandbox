#!/usr/bin/env python3
"""
Sort Objects by Attributes
"""

import collections
import operator


def show_list(the_list, label):
    print(f"# {label}")
    for element in the_list:
        print(f"  {element}")
    print()


if __name__ == "__main__":
    Person = collections.namedtuple("Person", "name uid")
    group = [Person("John", 456), Person("Karen", 234), Person("Amanda", 981)]

    show_list(group, "Original")

    group.sort(key=operator.attrgetter("name"))
    show_list(group, "Sorted by name")

    group.sort(key=operator.attrgetter("uid"))
    show_list(group, "Sorted by user ID")
