#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
From Raymond Hettinger
How to make a counter that is also keeping track of order
"""

from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == '__main__':
    d = OrderedCounter('ababcabcd')
    print(d)
