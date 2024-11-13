#!/usr/bin/env python

from pprint import pprint


class Entity(object):
    def greet(self):
        print("I am an entity")


class Animal(Entity):
    def greet(self):
        print("I am an animal")


class Creature(Entity):
    pass


class Dog(Creature, Animal):
    def greet(self):
        super().greet()
        print("I am a dog")


class Cat(Animal, Creature):
    def greet(self):
        super().greet()
        print("I am a cat")


if __name__ == "__main__":
    d = Dog()
    d.greet()
    pprint(Dog.__mro__)
    print("---")

    c = Cat()
    c.greet()
    pprint(Cat.__mro__)
