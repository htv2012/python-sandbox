"""Facility for simplifying ignoring of exceptions"""

from contextlib import contextmanager


@contextmanager
def ignore_exceptions(*exceptions):
    try:
        yield
    except exceptions:
        pass
