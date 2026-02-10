from dataclasses import dataclass
from typing import Protocol


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


def print_name(obj: HasName):
    print(obj.name)


def main():
    print_name(User("anna"))
    print_name(Net("private"))
    print_name(Foo("bar"))  # Static analysis will flag this


if __name__ == "__main__":
    main()
