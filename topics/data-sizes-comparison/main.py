import collections
import dataclasses
import types
import typing

from pympler import asizeof

UserNamedTupleFromCollections = collections.namedtuple(
    "UserNamedTupleFromCollections", "uid,alias,is_admin,shell"
)


class UserNamedTupleFromTyping(typing.NamedTuple):
    uid: int
    alias: str
    is_admin: bool
    shell: str


@dataclasses.dataclass
class UserDataclass:
    uid: int
    alias: str
    is_admin: bool
    shell: str


@dataclasses.dataclass(slots=True)
class UserDataclassWithSlots:
    uid: int
    alias: str
    is_admin: bool
    shell: str


@dataclasses.dataclass(frozen=True)
class UserDataclassFrozen:
    uid: int
    alias: str
    is_admin: bool
    shell: str


def main():
    users = [
        (
            (user := cls(uid=501, alias="karenc", is_admin=True, shell="/bin/bash")),
            asizeof.asizeof(user),
        )
        for cls in [
            UserNamedTupleFromCollections,
            UserNamedTupleFromTyping,
            UserDataclass,
            UserDataclassFrozen,
            UserDataclassWithSlots,
            types.SimpleNamespace,
        ]
    ]
    users.sort(key=lambda t: t[1])

    print("Size Object")
    print("---- ------")
    for user, size in users:
        print(f"{size:>4} {user.__class__.__name__}")

    print()
    print("Summary")
    print("- Named tuple from collections and typing are of the same size")
    print("- Named tuple is lighter weight than data classe")
    print("- Data class with slot is very light weight")
    print("- Adding frozen does not help reduce the size of a data class")


if __name__ == "__main__":
    main()
