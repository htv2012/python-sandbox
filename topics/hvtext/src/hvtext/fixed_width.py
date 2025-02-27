"""
This package parses rows of fixed-width columns of text, think of the
ouptut of the `ls -l` command.
"""

import csv
import fileinput
import functools
import itertools
import re
import sys


def guess_columns_for_one_row(row):
    """
    Given a row (line) of text, guess where the start indices are

    :param row: The row (line) of text
    :return: A set of indices where each column starts. If the caller
        wants the indices in order, they can call `sorted()`.
    """
    indices = set(matched.start() + 1 for matched in re.finditer(r"\S+", row))
    return indices


def guess_columns(rows):
    """
    Given a number of rows, guess the start indices for the columns. The
    indices are 1-based, i.e. the first index is 1.

    :param rows: The rows of text
    :return: A sorted list of indices indicating the start of the columns
    """
    indices = functools.reduce(
        lambda a, b: a.intersection(b), map(guess_columns_for_one_row, rows)
    )
    return sorted(indices)


def create_splitter(start_indices):
    """
    Create a splitter to split rows with fixed-width columns. The
    *start_indices* parameter is a list of start indices. Since we often
    work with text columns and view them in editors, a 1-based index is
    more convenient, i.e. the first column is 1.
    """
    # Turn 1-base to 0-base indices
    start_indices = [i - 1 for i in start_indices]

    start_indices.append(None)
    left = iter(start_indices)
    right = iter(start_indices)
    next(right)
    fields = [slice(a, b) for a, b in zip(left, right)]

    def split(line):
        return [line[field].strip() for field in fields]

    return split


def split_rows(rows, start_indices=None):
    """
    Given a sequence of rows and a list of start indices, return a list
    of list where each inner list represent a splitted row

    :param rows: Any iterable representing the rows of text
    :start_indices: A list of 1-based indices representing the start
        columns. A value of None will tell the function to guess the
        columns itself.
    :return: A generator object which returns the splitted rows
    """
    if start_indices is None:
        rows_to_guess, rows = itertools.tee(rows)
        start_indices = guess_columns(rows_to_guess)

    splitter = create_splitter(start_indices)
    return map(splitter, rows)


def main():
    """Module entry: Turn fixed-width rows into CSV"""
    rows = split_rows(fileinput.input())
    writer = csv.writer(sys.stdout)
    writer.writerows(rows)


if __name__ == "__main__":
    main()
