# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:33:08 2015

@author: haiv
"""

from collections import OrderedDict


class Cache(OrderedDict):
    def __init__(self, size=100, *args, **kwargs):
        super(Cache, self).__init__(*args, **kwargs)
        self.size = size

    def __setitem__(self, key, value):
        super(Cache, self).__setitem__(key, value)
        if len(self) > self.size:
            self.popitem(last=False)


if __name__ == "__main__":
    c = Cache(3)
    c["a"] = 5
    c["b"] = 7
    c["c"] = 9
    print(c)

    print(("a:", c["a"]))

    c["d"] = 11
    c["e"] = 13
    print(c)

    c["c"] = 99
    print(c)
