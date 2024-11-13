#!/usr/bin/env python
# encoding: utf-8
"""
fromfile_prefix_chars.py

Demo: use of text file to store arguments

Created by Hai Vu on 2013-03-12.
Copyright (c) 2013 High View Software. All rights reserved.
"""

import sys
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="fromfile_prefix_chars demo", fromfile_prefix_chars="@"
    )
    parser.add_argument(
        "-v", "--verbose", help="verbose output from crawler", action="store_true"
    )
    parser.add_argument("-o", "--output")
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    print("Input:   {}".format(args.input))
    print("Output:  {}".format(args.output))
    print("Verbose: {}".format(args.verbose))
