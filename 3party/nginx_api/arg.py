#!/usr/bin/env python3
import argparse
import sys

# parser = argparse.ArgumentParser()
# parser.add_argument("-d", "--display-name", default="")
# parser.add_argument("-D", "--description", default="")
# parser.add_argument("-t", "--tags", action="append")
# parser.add_argument("name")
# options = parser.parse_args()
# print(options)

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile")
# parser.add_argument("-D", "--description", default="")
# parser.add_argument("-t", "--tags", action="append")
# parser.add_argument("name")
options = parser.parse_args()

if options.infile:
    print(f"file: {options.infile}")
else:
    print("Invoke editor to edit")
