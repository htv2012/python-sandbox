#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import enum

if __name__ == "__main__":
    # Use auto() when we don't care about the value, only the names

    class Color(enum.Enum):
        red = enum.auto()
        green = enum.auto()
        blue = enum.auto()

    class Color2(enum.Enum):
        red = enum.auto()
        green = enum.auto()
        blue = enum.auto()

    for c in Color:
        print("{} = {}".format(c.name, c.value))
    print("---")

    for c in Color2:
        print("{} = {}".format(c.name, c.value))
    print("---")
