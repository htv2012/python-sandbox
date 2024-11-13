#!/usr/bin/env python

import csv


def apply_conversions(iterable, conversions):
    """
    Takes an iterable (list, tuple, ...) and a list of conversions and
    convert each element. Return the converted tuple.

    Example:
    >>> apply_conversions(['1.5', '3', 'hello'], (float, int, str))
    (1.5, 3, 'hello')
    """
    for row in iterable:
        converted = tuple(convert(cell) for convert, cell in zip(conversions, row))
        yield converted


if __name__ == '__main__':
    rows = [
        '501,haiv,4.5',
        '502,tracyv,3.7',
        '503,lynnv,4.8',
        '504,ericav,3.8',
    ]

    reader = csv.reader(rows)
    for row in apply_conversions(reader, (int, str, float)):
        print(row)
