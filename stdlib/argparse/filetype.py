#!/usr/bin/env python
# using FileType from argparse. We are going to read from a file and
# write to another while expand all environment variables.
# Examples:
#     filetype.py filetype_input
#     filetype.py -o filetype_output.txt filetype_input

import argparse
import os
import sys


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--outfile", type=argparse.FileType("wb"), default=sys.stdout
    )
    parser.add_argument("infile", type=argparse.FileType("rb"))
    return parser.parse_args()


def expand_variables(infile, outfile):
    for line in infile:
        line = os.path.expandvars(line)
        outfile.write(line)


def main():
    options = parse_command_line()
    expand_variables(options.infile, options.outfile)


if __name__ == "__main__":
    main()
