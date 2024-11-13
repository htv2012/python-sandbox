#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
From Raymond Hettinger
Demonstrates the MRO
"""

import os
import sys


class Adam(object):
    pass


class Eve(object):
    pass


# Raymond's Family
class Ramon(Adam, Eve):
    pass


class Gayle(Adam, Eve):
    def greet(self):
        print("Gayle")


class Raymond(Ramon, Gayle):
    pass


# Rachel's Family
class Dennis(Adam, Eve):
    pass


class Sharon(Adam, Eve):
    pass


class Rachel(Dennis, Sharon):
    def greet(self):
        print("Rachel")


# Raymond and Rachel's Family
class Matthew(Raymond, Rachel):
    pass


def main():
    matthew = Matthew()
    print("Matthew's Method Resolution Order (MRO):")
    for klass in Matthew.mro():
        print("-", klass.__name__)

    print("\nmathiew greet:")
    matthew.greet()


if __name__ == "__main__":
    main()
