#!/usr/bin/env python3
"""
A Python skeleton script
"""
import typing


class Credential(typing.NamedTuple):
    username: str
    password: str

    def __str__(self):
        return f"{self.username}:{self.password}"


def main():
    """ Entry """
    credential = Credential("jdoe", "i4got")
    url = f"{credential}@foobar.com"
    print(url)


if __name__ == '__main__':
    main()
