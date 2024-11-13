#!/usr/bin/env python3
"""
Parses /etc/os-release, /etc/product, ...
"""
import fileinput
import pprint

import kvlib


def main():
    """ Entry """
    text = "".join(fileinput.input())
    print("Text to parsed:")
    print(text)
    print("-" * 80)

    print("Parsed:")
    dict_object = kvlib.parse(text)
    pprint.pprint(dict_object)


if __name__ == '__main__':
    main()
