#!/usr/bin/env python

import unittest
from functools import reduce


def replace_multiple_patterns(text, patterns):
    """Given some text and a list of old-new patterns, replace.
    Example:
    >>> replace_multiple_patterns('ab', [('a', 'x'), ('b', 'y')])
    'xy'

    :param text: The text to be replaced
    :param patterns: a list of old-new pairs
    """
    return reduce(lambda s, pattern: s.replace(*pattern), patterns, text)


class ReplaceTest(unittest.TestCase):
    def test_one_pattern(self):
        self._replace_and_verify(
            [("doo", "_WHOO_HOO")], "yabadabadoo", "yabadaba_WHOO_HOO"
        )

    def test_multiple_patterns(self):
        self._replace_and_verify(
            [("yaba", "scooby"), ("daba", "dobe")], "yabadabadoo", "scoobydobedoo"
        )

    def test_empty_string(self):
        self._replace_and_verify([("yaba", "scooby"), ("daba", "dobe")], "", "")

    def _replace_and_verify(self, patterns, original, expected):
        actual = replace_multiple_patterns(original, patterns)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
