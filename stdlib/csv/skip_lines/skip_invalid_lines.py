#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
How to skip bad lines (or other invalid lines) in a csv file
"""

import csv
import sys

sys.path.append("..")
from logger import logger


def is_good_line(raw_line):
    # A good line is not empty
    return bool(raw_line.strip())


with open("data.csv", "rb") as f:
    reader = csv.reader(filter(is_good_line, f))
    for row in reader:
        logger.info("%r", row)
