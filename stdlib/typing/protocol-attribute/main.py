from dataclasses import dataclass
from typing import List, Protocol


class HasName(Protocol):
    name: str


@dataclass
class User:
    name: str


@dataclass
class Net:
    name: str


@dataclass
class Foo:
    bar: str


def get_names(objects: List[HasName]) -> List[str]:
    return [obj.name for obj in objects]


users = [User(f"user-{i}") for i in range(3)]
print(get_names(users))

foos = [Foo(f"foo-{i}") for i in range(3)]
print(get_names(foos))
