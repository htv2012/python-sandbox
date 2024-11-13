#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
How to skip bad lines (or other invalid lines) in a csv file
"""

import csv
import sys

sys.path.append("..")
from logger import logger


def is_good_line(row_as_list):
    good = len(row_as_list) == 2
    if not good:
        logger.debug("... Bad: %r", row_as_list)
    return good


with open("bad.csv", "rb") as f:
    reader = filter(is_good_line, csv.reader(f))
    for row in reader:
        logger.info("%r", row)
