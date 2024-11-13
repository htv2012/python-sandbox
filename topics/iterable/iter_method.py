#!/usr/bin/env python
"""
Making a class object iterable by adding __iter__
"""


class Band(object):
    def __init__(self, *members):
        self._members = members

    def __iter__(self):
        return iter(self._members)


if __name__ == "__main__":
    band = Band("John", "Paul", "George", "Ringo")
    for member in band:
        print(member)
