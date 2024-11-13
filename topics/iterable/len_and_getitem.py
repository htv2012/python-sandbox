#!/usr/bin/env python
"""
Making a class object iterable by adding __len__ and __getitem__
"""


class Band(object):
    def __init__(self, *members):
        self._members = members

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]


if __name__ == "__main__":
    band = Band("John", "Paul", "George", "Ringo")
    for member in band:
        print(member)
