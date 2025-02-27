#!/usr/bin/env python
"""
Demonstrate when guessing does not work
"""

from hvtext import fixed_width

OUTPUT = """
drwxr-xr-x 3 haiv haiv 4096 Jun  8 14:09 fixed_width
-rwxr-xr-x 1 haiv haiv  278 Jun  8 14:09 guess.py
-rwxr-xr-x 1 haiv haiv  441 Jun  8 14:09 parse_fixed_width_files.py
drwxr-xr-x 2 haiv haiv 4096 Jun  8 08:19 __pycache__
-rw-r--r-- 1 haiv haiv  160 Jun  8 14:09 table.txt
""".strip().splitlines()


def main():
    """Entry point"""
    # Here we try to guess the columns, but not really work because one
    # of the column is right-justified.
    print("WITH GUESSING")
    for row in fixed_width.split_rows(OUTPUT):
        print(row)

    # Since some of the columns are right-justified, we cannot guess,
    # but exciplitly specify the columns manually
    print("\nWITH EXPLICIT COLUMN DEFINITIONS")
    indices = [1, 12, 14, 19, 24, 29, 34, 36, 42]
    for row in fixed_width.split_rows(OUTPUT, indices):
        print(row)


if __name__ == "__main__":
    main()
