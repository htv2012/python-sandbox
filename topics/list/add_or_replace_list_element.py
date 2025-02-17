#!/usr/bin/env python3
"""
whatis: add-or-replace operation
"""

import collections

User = collections.namedtuple("User", ["uid", "alias"])


def add_or_replace(users, new_user):
    for index, user in enumerate(users):
        if new_user.uid == user.uid:
            users[index] = new_user
            return

    users.append(new_user)


def show(label, users):
    print()
    print(f"# {label}")
    for user in users:
        print(f"  {user}")


def main():
    """Entry"""
    users = [
        User(501, "anna"),
        User(502, "karen"),
        User(504, "john"),
    ]
    show("Original", users)

    new_user = User(502, "kim")
    add_or_replace(users, new_user)
    show(f"Add {new_user} or replace the old one", users)

    new_user = User(509, "mike")
    add_or_replace(users, new_user)
    show(f"Add {new_user} or replace the old one", users)


if __name__ == "__main__":
    main()
