#!/usr/bin/env python3
import collections

import toolz

User = collections.namedtuple("User", "uid, alias, shell")


def convert_uid(row):
    return int(row[0]), row[1], row[2]


def to_user(row):
    return User(*row)


def main():
    data = [
        (501, "karen", "zsh"),
        (502, "anna", "bash"),
    ]

    print("\n\nCOMPOSE DEMO")
    normalize = toolz.compose(to_user, convert_uid)
    rows = map(normalize, data)
    for row in rows:
        print(f"- {row!r}")


if __name__ == "__main__":
    main()
