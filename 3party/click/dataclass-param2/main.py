import dataclasses
import enum
from typing import List, Set

import click

from clicklib import dataclass_options


class Department(enum.Enum):
    ENGINEER = "engineer"
    MARKETING = "marketing"


@dataclasses.dataclass
class UserInfo:
    uid: int
    alias: str
    department: Department
    admin: bool = True
    security_score: float = 0.75
    groups: List[str] = dataclasses.field(default_factory=list)
    keys: Set[int] = dataclasses.field(default_factory=set)


@click.command
@dataclass_options(UserInfo, name="user")
@dataclass_options(UserInfo, name="receiver")
def main(user, receiver):
    """Demo of how to construct a data class from command line."""
    print(f"{user=}")
    print(f"{receiver=}")


if __name__ == "__main__":
    main()
