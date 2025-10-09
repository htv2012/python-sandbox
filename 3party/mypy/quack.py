#!/usr/bin/env python3
import types
from typing import Protocol


class Quacker(Protocol):
    def quack(self):
        pass


class Duck:
    def quack(self):
        print("quack")


class Dog:
    def bark(self):
        print("woof")

    def __getattr__(self, name):
        if name == "quack":
            return self.bark


def cat():
    def meow():
        print("meow")

    return types.SimpleNamespace(quack=meow)


def sound(d: Quacker):
    d.quack()


def main():
    for d in [Duck(), Dog(), cat()]:
        sound(d)


if __name__ == "__main__":
    main()
