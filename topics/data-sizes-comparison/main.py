import collections
import dataclasses
import types
import typing

from pympler import asizeof

UserNamedTuple = collections.namedtuple("UserNamedTuple", "uid,alias,is_admin,shell")


class UserNamedTuple2(typing.NamedTuple):
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


users = [
    UserNamedTuple(501, "karenc", True, "/bin/bash"),
    UserNamedTuple2(501, "karenc", True, "/bin/bash"),
    UserDataclass(501, "karenc", True, "/bin/bash"),
    UserDataclassFrozen(501, "karenc", True, "/bin/bash"),
    UserDataclassWithSlots(501, "karenc", True, "/bin/bash"),
    types.SimpleNamespace(uid=501, alias="karenc", is_admin=True, shell="/bin/bash"),
]

print("Size Object")
print("---- ------")
for user in users:
    print(f"{asizeof.asizeof(user):>4} {user}")

print()
print("Summary")
print("- Named tuple from collections and typing are of the same size")
print("- Named tuple is lighter weight than data classe")
print("- Data class with slot is very light weight")
print("- Adding frozen does not help reduce the size of a data class")
