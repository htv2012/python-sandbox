#!/usr/bin/env python
"""
Parse key-value blocks of text
"""

from . import discard


def _split_fields(text, separator):
    """
    A helper to split a line of text into fields
    """
    return [field.strip() for field in text.split(separator, 1)]


def parse(iterable, separator="="):
    """
    Given an series of lines, each representing a pair of key and
    vaiues and a separator, parse the lines and return a dictionary

    :param iterable: Any iterable representing a series of text lines.
        This can be a list of lines, a generator object, a readable
        file handle; for short anything that can be iterated upon.
    :param separator: A single character representing the field
        separator
    :return: A dictionary represent the keys and values
    """
    # Skip blanks and comments
    iterable = discard.blank(iterable)
    iterable = discard.comment(iterable)

    parsed = dict(_split_fields(line, separator) for line in iterable)
    return parsed
