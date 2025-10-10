#!/usr/bin/env python3
from typing import Protocol


class Quacker(Protocol):
    def quack(self):
        pass


class Duck:
    def quack(self):
        print("quack")


class Dog:
    def quack(self):
        print("woof")


class Cat:
    def quack(self):
        print("meow")


def sound(d: Quacker):
    d.quack()


def main():
    for d in [Duck(), Dog(), Cat()]:
        sound(d)


if __name__ == "__main__":
    main()
