"""
OrderedSet implemented using OrderedDict
"""

import collections


class OrderedSet(collections.Set):
    def __init__(self, iterable=None):
        self.map = collections.OrderedDict()
        for item in iterable or []:
            self.map[item] = 1

    def __iter__(self):
        return iter(self.map)

    def __contains__(self, item):
        return item in self.map

    def __len__(self):
        return len(self.map)

    def add(self, item):
        self.map.setdefault(item, 1)
