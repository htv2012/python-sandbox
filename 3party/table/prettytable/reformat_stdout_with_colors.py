#!/usr/bin/env python3
"""
Reformat stdout using pretty table
"""

from banner import banner
from colors import colorize
from tablelib import tsv_table


def show_results(results):
    print("Test\tResult")
    for name, result in results:
        result = colorize(result)
        print(f"{name}\t{result}")


def main():
    """Entry"""
    results = [
        ("Check Connection", "Passed"),
        ("Check Banner", "Passed"),
        ("Check User Login", "Failed"),
        ("Check Cookies", "Blocked"),
        ("Check Endpoints", "Passed with warnings"),
    ]

    banner("Raw Output")
    show_results(results)

    banner("Formatted Output")
    with tsv_table():
        show_results(results)


if __name__ == "__main__":
    main()
