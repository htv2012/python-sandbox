#!/usr/bin/env python3
"""Chain multiple CSV files"""
import argparse
import contextlib
import csv
import sys


def chain_files(*filenames, encoding="utf-8"):
    """
    Chain lines in files together.

    The first line of the first file is the column headers. Skip
    the headers in subsequent files.
    """
    headers = None
    for filename in filenames:
        with open(filename, encoding=encoding) as stream:
            # Examine the first row: Is this te column headers?
            try:
                row = next(stream)
            except StopIteration:
                continue
            if headers is None:
                headers = row
                yield headers
            elif row != headers:
                yield row

            yield from stream


parser = argparse.ArgumentParser()
parser.add_argument("input", nargs="+")
parser.add_argument("-o", "--output")

options = parser.parse_args()
reader = csv.reader(chain_files(*options.input))

with contextlib.ExitStack() as stack:
    if options.output is None:
        output_stream = sys.stdout
    else:
        output_stream = open(options.output, "w", encoding="utf-8")
        stack.enter_context(output_stream)

    writer = csv.writer(output_stream)
    writer.writerows(reader)
