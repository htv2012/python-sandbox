#!/usr/bin/env python3
"""
A CLI interface into pinboard
"""
import argparse
import collections
import collections.abc
import inspect
import json
import textwrap


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', '--debug-level2', help='foo bar')
    sub_parsers = parser.add_subparsers(dest='mycmd', required=True)

    sub_parsers.add_parser('notes')
    sub_parsers.add_parser('ls')
    sub_parsers.add_parser('export')

    argument_parser = sub_parsers.add_parser('new')
    argument_parser.add_argument('-t', '--tags')
    argument_parser.add_argument(
        '-s', '--shared',
        default='no',
        action='store_const',
        const='yes')
    argument_parser.add_argument(
        '-r', '--toread',
        default='no',
        action='store_const',
        const='yes')
    argument_parser.add_argument('url')
    argument_parser.add_argument('description')

    argument_parser = sub_parsers.add_parser('rm')
    argument_parser.add_argument('urls', nargs='+')

    ap = sub_parsers.add_parser('foo')
    ap.add_argument('-a', '--athing')
    ap.add_argument('-b', '--bthing')
    ap.add_argument('abc')
    ap.add_argument('def')

    options = parser.parse_args()
    return options

def main():
    """
    Entry
    """
    options = parse_command_line()


if __name__ == '__main__':
    main()
