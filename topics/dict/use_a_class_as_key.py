#!/usr/bin/env python3
"""Use a class as key to a dictionary.

In order to be a key, an object must have a hash value that is
constant.
"""


class User:
    def __init__(self, uid, alias):
        self.uid = uid
        self.alias = alias

    def __hash__(self) -> int:
        # Hash of this object depends on UID and we
        # assume that UID is unchanged.
        return hash(self.uid)

    def __repr__(self):
        return f"{self.__class__.__name__}(uid={self.uid!r}, alias={self.alias!r})"


def main():
    """Entry"""
    user1 = User(uid=501, alias="karen")
    user2 = User(uid=502, alias="anna")
    scores = {
        user1: 98,
        user2: 97,
    }

    print(scores)


if __name__ == "__main__":
    main()
