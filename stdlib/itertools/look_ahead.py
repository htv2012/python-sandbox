#!/usr/bin/env python
"""
Prints all non-comment lines, except for the last one.
Use `tee` to accomplish
"""

from itertools import tee, zip_longest

if __name__ == "__main__":
    with open("data.txt") as f:
        current_buffer, next_buffer = tee(f)
        next(next_buffer)
        for current_line, next_line in zip_longest(
            current_buffer, next_buffer, fillvalue="#"
        ):
            if not current_line.startswith("#") and not next_line.startswith("#"):
                print(current_line, end=" ")
