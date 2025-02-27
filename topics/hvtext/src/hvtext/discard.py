#!/usr/bin/env python
"""
This module contains functions to discard unwanted lines such as empty
lines, commented lines from a collection of lines.
"""


def comment(lines, comment_char="#"):
    """
    Given a list of lines, discard those lines that starts with a comment

    :param lines: Any iterable representing the lines of text
    :param comment_char: A character representing a comment character
    :return: A generator object which generates those lines that are
        not comment lines
    """
    return filter(lambda line: not line.strip().startswith(comment_char), lines)


def blank(lines):
    """
    Given a list of lines, discard those that are blank

    :param lines: Any iterable representing the lines of text
    :return: A generator object which generates those lines that are
        not blank
    """
    return filter(lambda line: line.strip(), lines)
