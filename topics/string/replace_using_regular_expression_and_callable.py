#!/usr/bin/env python3
"""
re.sub() can take a string as the replacement, or it can take in a
function. This script demonstrates the later.
"""

import re


class AddSerial(object):
    def __init__(self, serial=1):
        self.serial = serial

    def __call__(self, sre_match):
        text = sre_match.group()
        text = "{}[{}]".format(text, self.serial)
        self.serial += 1
        return text


def main():
    """Entry"""
    s = "UPPER PYTHON, Cap Python, lower python"
    new_s = re.sub("python", AddSerial(), s, flags=re.IGNORECASE)
    print("Original:  ", s)
    print("Serialized:", new_s)


if __name__ == "__main__":
    main()
