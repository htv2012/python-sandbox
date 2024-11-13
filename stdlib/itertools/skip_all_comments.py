#!/usr/bin/env python

"""
Skip commented lines using ifilterfalse()
"""

import itertools

LINES = """
# Name: Demo
# Last Modified: yesterday
line 1
# remove me
line 2
# me too
""".strip().splitlines()


def is_comment(text):
    return text.strip().startswith("#")


def main():
    """Entry"""
    # Show original
    print("\n--- Original Contents ---")
    print("\n".join(LINES))

    # Skip all comments
    print("\n--- Skip All Comments ---")
    print("\n".join(itertools.filterfalse(is_comment, LINES)))


if __name__ == "__main__":
    main()
