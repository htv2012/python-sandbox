#!/usr/bin/env python
"""
Tests the hvtext.discard.comment() function
"""

from hvtext.discard import comment


def test_default_comment():
    """Discard default comment char"""
    input_lines = ["# comment 1", "line1", "# indented comment", "# comment 2", "line2"]
    expected = ["line1", "line2"]
    actual = list(comment(input_lines))
    assert expected == actual


def test_non_default():
    """Discard non-default comments"""
    input_lines = ["; comment 1", "line1", "  ; comment 2", "line2"]
    expected = ["line1", "line2"]
    actual = list(comment(input_lines, ";"))
    assert expected == actual


def test_non_stand_alone_comment():
    """Do not discard comments that are not standing alone"""
    input_lines = ["; comment 1", "line1  # OK", "  ; comment 2", "line2"]
    expected = ["line1  # OK", "line2"]
    actual = list(comment(input_lines, ";"))
    assert expected == actual
