"""
Demo: Convert JSON string from command line arguments into objects

There are two different ways to validate the arguments. The Server
class use the `from_json` class method, while the User class uses the
`__post_init__` method from data clasess. The both achieve the same
result.
"""

import contextlib
import dataclasses
import enum
from typing import List


class Subject(enum.Enum):
    MATH = ("Applied Math", 3)
    ENGLISH = ("English", 4)
    HISTORY = ("History", 4)

    def __init__(self, name, weight):
        self._value_ = name
        self.weight = weight

    @classmethod
    def from_json(cls, json_object: str):
        name, _, weight = json_object.partition(",")

        # found = next((m for m in Subject if m.value == name), None)
        found = cls[name.upper()]
        if found is None:
            raise ValueError()

        with contextlib.suppress(ValueError):
            found.weight = int(weight)
        return found


@dataclasses.dataclass
class Server:
    host: str
    port: int
    secured: bool

    @classmethod
    def from_json(cls, json_object):
        port = json_object["port"]
        secured = json_object["secured"]

        if not isinstance(port, int):
            raise TypeError(f"port is not int: {port!r}")
        if not isinstance(secured, bool):
            raise TypeError(f"secured is not bool: {secured!r}")

        return cls(**json_object)


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    is_admin: bool = False
    groups: List[str] = dataclasses.field(default_factory=list)

    @classmethod
    def from_json(cls, json_object):
        uid = json_object["uid"]
        is_admin = json_object["is_admin"]
        groups = json_object["groups"]

        if not isinstance(uid, int):
            raise TypeError(f"UID is not int: {uid!r}")
        if not isinstance(is_admin, bool):
            raise TypeError(f"is_admin is not bool: {is_admin!r}")
        if not isinstance(groups, list):
            raise TypeError(f"groups is not a list of strings: {groups!r}")
        return cls(**json_object)


@dataclasses.dataclass
class Testbed:
    """A combo class, more complex."""

    server: Server
    user: User

    @classmethod
    def from_json(cls, data):
        server = Server.from_json(data["server"])
        user = User(**data["user"])
        return cls(server=server, user=user)
