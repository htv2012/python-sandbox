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


def info(obj):
    print()
    print(f"Object: {obj}")
    print(f"size: {asizeof.asizeof(obj)}")


users = [
    UserNamedTuple(501, "karenc", True, "/bin/bash"),
    UserNamedTuple2(501, "karenc", True, "/bin/bash"),
    UserDataclass(501, "karenc", True, "/bin/bash"),
    types.SimpleNamespace(uid=501, alias="karenc", is_admin=True, shell="/bin/bash"),
]
for user in users:
    info(user)
