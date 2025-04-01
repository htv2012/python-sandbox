#!/usr/bin/env python3
"""
Demo: Update a real dict from a dict-like object
"""

import collections.abc


class User(collections.abc.Mapping):
    def __init__(self, uid, alias, shell):
        super().__init__()
        self.uid = uid
        self.alias = alias
        self.shell = shell

    def __getitem__(self, key):
        if key == "uid":
            return self.uid
        elif key == "alias":
            return self.alias
        elif key == "shell":
            return self.shell
        raise KeyError()

    def __iter__(self):
        return iter(["uid", "alias", "shell"])

    def __len__(self):
        return 3

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"uid={self.uid!r}"
            f", "
            f"alias={self.alias!r}"
            f", "
            f"shell={self.shell!r}"
            f")"
        )


print("\nObject u:")
u = User(501, "karen", "zsh")
print(u)

print("\nDictionary d:")
d = {"uid": 502, "isAdmin": True}
print(d)

print("\nUpdate d with u:")
d.update(u)
print(d)
print()
