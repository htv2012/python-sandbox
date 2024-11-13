#!/usr/bin/env python3
"""Tabulate a list of namedtuple's."""
import tabulate


def main():
    """Entry"""
    data = [
        ["UID", "Alias", "Shell"],
        [501, "peter", "zsh"],
        [502, "paul", "bash"],
        [503, "mary", "dash"],
    ]
    print(tabulate.tabulate(data, headers="firstrow"))


if __name__ == "__main__":
    main()
