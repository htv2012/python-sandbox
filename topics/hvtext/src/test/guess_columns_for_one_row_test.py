#!/usr/bin/env python
"""
Test the `guess_columns_for_one_row(row)` function
"""

from hvtext.fixed_width import guess_columns_for_one_row


def test_normal_case():
    """Under a normal usage, guess the right columns"""
    expected = {1, 10, 15}
    actual = guess_columns_for_one_row("one      two  three")
    assert expected == actual


def test_symbols_in_column():
    """Symbols at the start, middle, and end of columns"""
    expected = {1, 9, 16}
    actual = guess_columns_for_one_row("%one    {two}  thr/ee")
    assert expected == actual


def test_lines_with_initial_spaces():
    """Correctly handle lines with initial spaces"""
    expected = {3, 12, 17}
    actual = guess_columns_for_one_row("  one      two  three")
    assert expected == actual


def test_trailing_newline():
    """Ignore trailing new lines"""
    expected = {1, 10, 15}
    actual = guess_columns_for_one_row("one      two  three\n")
    assert expected == actual


def test_single_column():
    """Correctly handle case where there is a single column"""
    expected = {1}
    actual = guess_columns_for_one_row("single_column\n")
    assert expected == actual


def test_duplicate_cells():
    """Cells with the same names"""
    expected = {1, 5, 9, 13}
    actual = guess_columns_for_one_row("one two two three\n")
    assert expected == actual
