#!/usr/bin/env python3
"""
Reformat stdout using pretty table
"""

from tablelib import tsv_table


def main():
    """Entry"""
    print("\n#\n# Use first row of output as headers\n#\n")
    with tsv_table():
        print("UID\tAlias\tShell")
        print("501\tanna\tbash")
        print("502\tkaren\tzsh")
        print("1011\tjake\tzsh")

    print("\n#\n# Explicitly specify the headers\n#\n")
    with tsv_table(headers=["User ID", "User Alias", "Shell"]):
        print("501\tanna\tbash")
        print("502\tkaren\tzsh")
        print("1011\tjake\tzsh")


if __name__ == "__main__":
    main()
