#!/usr/bin/env python3
import dataclasses
import typing

import deepdiff


@dataclasses.dataclass
class User:
    uid: int
    alias: str


@dataclasses.dataclass
class Group:
    gid: int
    name: str
    members: typing.List[User]


def main():
    """Entry"""
    g1 = Group(
        gid=1001, name="Carpenters", members=[User(501, "karen"), User(502, "john")]
    )
    g2 = Group(
        gid=1001,
        name="Carp.",
        members=[User(501, "caren"), User(502, "john"), User(503, "anna")],
    )
    dd = deepdiff.DeepDiff(g1, g2, ignore_order=True)

    print("\n# g1")
    print(g1)

    print("\n# g2")
    print(g2)

    print("\n# diff")
    print(dd.pretty())


if __name__ == "__main__":
    main()
