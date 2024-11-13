#!/usr/bin/env python
"""
doctest_example.py
How to run the tests:

    python -m doctest doctest_example.py

"""


def foo(name):
    """
    >>> foo("me")
    '[me]'

    >>> foo('bar')
    '[bart]'
    """
    return "[{}]".format(name)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
