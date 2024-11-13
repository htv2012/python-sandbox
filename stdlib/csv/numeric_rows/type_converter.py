#!/usr/bin/env python
"""
Convert string to different types
"""
import csv
from functools import partial

from_hex_str = partial(int, base=16)
from_oct_str = partial(int, base=8)
from_bin_str = partial(int, base=2)


def typed_reader(iterable, converters, **reader_options):
    reader = csv.reader(iterable, **reader_options)
    for row in reader:
        new_row = tuple(
            converter(cell)
            for converter, cell in zip(converters, row)
        )
        yield new_row
