#!/usr/bin/env python

"""
Return in finally clause
From Raymond Hettinger
"""


def return_in_finally_clause():
    """Returns 42"""
    try:
        raise KeyError
    finally:
        return 42


def return_outside_finally_clause():
    """Does not have a chance to return value (2)"""
    value = 1
    try:
        raise KeyError
    finally:
        value = 2
    return value


if __name__ == "__main__":
    # This returns 42
    print("Return value:", return_in_finally_clause())

    # This causes exception
    print("Return value:", return_outside_finally_clause())
