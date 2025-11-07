"""Pluralize words"""

import re


def format_count(count: int, word: str):
    """Format a count and word a string.

    Reference: https://www.geeksforgeeks.org/python/python-program-to-convert-singular-to-plural/

    >>> format_count(5, "monkey")
    '5 monkeys'

    >>> format_count(2, "batch")
    '2 batches'
    """
    if count < 2:
        pass
    elif re.search("[sxz]$", word) or re.search("[^aeioudgkprt]h$", word):
        word = f"{word}es"
    elif re.search("[^aeiou]y$", word):
        word = re.sub("y$", "ies", word)
    else:
        word = f"{word}s"

    return f"{count} {word}"
