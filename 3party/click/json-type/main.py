"""
Demo: Convert JSON string from command line arguments into objects

There are two different ways to validate the arguments. The Server
class use the `from_json` class method, while the User class uses the
`__post_init__` method from data clasess. The both achieve the same
result.
"""

import dataclasses
import json
from typing import List

import click

from clicklib import JsonParamType


@dataclasses.dataclass
class Server:
    host: str
    port: int
    secured: bool

    @classmethod
    def from_json(cls, **kwargs):
        if not isinstance(port := kwargs["port"], int):
            raise TypeError(f"port is not int: {port!r}")
        if not isinstance(secured := kwargs["secured"], bool):
            raise TypeError(f"secured is not bool: {secured!r}")
        return cls(**kwargs)


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    is_admin: bool = False
    groups: List[str] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.uid, int):
            raise TypeError(f"UID is not int: {self.uid!r}")
        if not isinstance(self.is_admin, bool):
            raise TypeError(f"UID is not bool: {self.is_admin!r}")


@click.command
@click.option("-s", "--server", type=JsonParamType(Server.from_json))
@click.option("-u", "--user", type=JsonParamType(User))
@click.option("--band", type=json.loads, help="Raw JSON")
def main(server: Server, user: User, band):
    if server:
        print(f"{server=}")
    if user:
        print(f"{user=}")
    if band:
        print(f"band={json.dumps(band, indent=4)}")


if __name__ == "__main__":
    main()
