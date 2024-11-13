#!/usr/bin/env python3
"""Tabulate a list of namedtuple's."""
import collections

import tabulate


def main():
    """Entry"""
    User = collections.namedtuple("User", "uid,alias,shell")
    data = [
        User(501, "peter", "zsh"),
        User(502, "paul", "bash"),
        User(503, "mary", "dash"),
    ]
    print(tabulate.tabulate(data, headers="keys"))


if __name__ == "__main__":
    main()
