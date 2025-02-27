#!/usr/bin/env python
"""
Test the hvtext.discard.blank() function
"""

from hvtext import discard


def test_normal_case():
    """A normal positive case"""
    input_lines = ["", "line1", "  \t  ", "line2"]
    expected = ["line1", "line2"]
    actual = list(discard.blank(input_lines))
    assert expected == actual
