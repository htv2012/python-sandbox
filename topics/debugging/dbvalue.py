#!/usr/bin/env python3
"""
A Python skeleton script
"""
import inspect
import re


def dbvalue(arg):
    """
    Prints out a value with file/line/function information
    """
    last_stack = inspect.stack()[1]
    # (<frame object at 0x7fcb1f65a750>, 'stack_frame.py', 15, 'foo', ['    dbvalue(arg1)\n'], 0)
    _, filename, lineno, function, code_context, _ = last_stack

    expression = "expression"
    for context in code_context:
        matched = re.search(r"dbvalue\((.*)\)", context)
        if matched is not None:
            expression = matched.group(1)
            break

    print(f"{filename}({lineno}) in {function}: {expression} = {arg!r}")


def foo(arg1, arg2):
    dbvalue(arg1)
    dbvalue(arg2 + 5)


def main():
    """ Entry """
    foo("hello", 9)
    dbvalue(__file__)



if __name__ == '__main__':
    main()

