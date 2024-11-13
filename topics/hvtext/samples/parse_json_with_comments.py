#!/usr/bin/env python
"""
Demo: Parse JSON file with comments
"""
import json
import pathlib

from hvtext import discard

DATA_PATH = pathlib.Path(__file__).with_name('json_with_comments.json')

def main():
    """ Entry """
    with open(DATA_PATH) as json_file:
        lines = '\n'.join(discard.comment(json_file))
        data = json.loads(lines)
        print(data)


if __name__ == '__main__':
    main()

