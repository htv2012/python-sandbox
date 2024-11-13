#!/usr/bin/env python3
"""
Simple script to write something to stdout and stderr, used by other
scripts as demo.
"""
import sys


def main():
    """ Entry """
    sys.stdout.write("This goes to stdout\n")
    sys.stdout.flush()

    sys.stderr.write("This goes to stderr\n")
    sys.stderr.flush()


if __name__ == '__main__':
    main()
