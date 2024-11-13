#!/usr/bin/env python3
"""
Displays a list of dicts
"""
import tabulate


def main():
    """Entry"""
    table = [
        dict(uid=501, alias="johnk", shell="bash"),
        dict(uid=502, alias="karenc", shell="zsh"),
    ]

    print(tabulate.tabulate(table, headers="keys"))


if __name__ == "__main__":
    main()
