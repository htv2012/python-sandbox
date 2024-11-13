#!/usr/bin/env python
import functools
import itertools


def _str2int(number_or_str):
    try:
        return int(number_or_str, 10)
    except ValueError:
        return number_or_str


def _make_equal_lengths(tuple1, tuple2):
    return itertools.zip_longest(tuple1, tuple2, fillvalue=0)


@functools.total_ordering
class Version:
    def __init__(self, version_str):
        self.version_str = version_str.strip()
        self.version_tuple = tuple(_str2int(n) for n in self.version_str.split('.'))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.version_str!r})"

    def __str__(self):
        return self.version_str

    def __eq__(self, other):
        for a, b in _make_equal_lengths(self.version_tuple, other.version_tuple):
            if a != b:
                return False
        return True

    def __lt__(self, other):
        for a, b in _make_equal_lengths(self.version_tuple, other.version_tuple):
            if a == b:
                pass
            elif a < b:
                return True
            else:
                return False
        return False
