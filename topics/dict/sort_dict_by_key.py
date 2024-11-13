#!/usr/bin/env python
"""Sort a list of dictionaries based on a common key."""

from operator import itemgetter
from pprint import pprint


def custom_getter(key):
    def get_value(dict_object):
        return dict_object[key]

    return get_value


def main():
    """Entry"""
    users = [
        dict(uid=502, first="Tate", last="Chandler"),
        dict(uid=501, first="John", last="Kimball"),
        dict(uid=503, first="Alice", last="Thompson"),
    ]

    print("\n# Original list:")
    pprint(users)

    print("\n# Sorted by first name:")
    pprint(sorted(users, key=lambda u: u["first"]))

    print("\n# Sorted by last name:")
    pprint(sorted(users, key=itemgetter("last")))

    print("\n# Sorted by UID:")
    pprint(sorted(users, key=custom_getter("uid")))


if __name__ == "__main__":
    main()
