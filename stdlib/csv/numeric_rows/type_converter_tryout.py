#!/usr/bin/env python
"""
Try out the type_converter module
"""
from type_converter import (
    typed_reader,
    from_hex_str,
    from_oct_str,
)


def main():
    converters = (str, int, float, from_hex_str, from_oct_str, float)
    with open('data.csv') as f:
        next(f)  # Get rid of the header row
        reader = typed_reader(f, converters)
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
