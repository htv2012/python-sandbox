#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python can provide the rest of the comparison if we provide eq, ne, and lt
"""


class User(object):
    def __init__(self, uid, alias):
        self.alias = alias
        self.uid = uid

    def __eq__(self, other):
        return self.uid == other.uid

    def __ne__(self, other):
        return self.uid != other.uid

    def __lt__(self, other):
        return self.uid < other.uid

    def __repr__(self):
        return "User(uid={!r}, alias={!r})".format(self.uid, self.alias)


if __name__ == "__main__":
    u1a = User(501, "john")
    u1b = User(501, "John Doe")
    u2 = User(502, "karen")

    assert u1a == u1b
    assert not (u1a != u1b)
    assert u2 > u1a
    assert u2 >= u1a
