#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
from collections import namedtuple


class NamedTupleReader(object):
    def __init__(self, iterable, dialect='excel', *args, **kwargs):
        self.reader = csv.reader(iterable, dialect=dialect, *args, **kwargs)

        # Read the first row and turn into a named tuple
        row = next(self.reader)
        self.RowType = namedtuple('Row', row)
        self.fieldnames = self.RowType._fields

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self.reader)
        row = self.RowType(*row)
        return row
