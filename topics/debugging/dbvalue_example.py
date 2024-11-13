#!/usr/bin/env python3
"""
A Python skeleton script
"""
import inspect
import re

import dbvalue


def foo(arg1, arg2):
    dbvalue.dbvalue(arg1)
    dbvalue.dbvalue(arg2 + 5)


def main():
    """ Entry """
    foo("hello", 9)
    dbvalue.dbvalue(__file__)



if __name__ == '__main__':
    main()

