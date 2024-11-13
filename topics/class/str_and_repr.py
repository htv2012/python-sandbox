#!/usr/bin/env python
# encoding: utf-8
"""
Created by Hai Vu on 2012-11-09.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.

Differences between __str__ and __repr__
* __repr__ aims to be unambigous
* __str__ aims to be readable
"""


class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def __repr__(self):
        return "Car({!r}, {!r}, {!r})".format(self.year, self.make, self.model)

    def __str__(self):
        return "{year} {make} {model}".format(**self.__dict__)


if __name__ == "__main__":
    c = Car(2004, "Toyota", "Camry")
    print(c)
    print(repr(c))
