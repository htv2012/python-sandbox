#!/usr/bin/env python3
"""Format all numbers in a text document with commas."""
import re


def format_with_comma(match: re.Match) -> str:
    number = int(match[0])
    return f"{number:,}"


DOCUMENT = """
Country: Tera Curva
Population: 5900000 people
Area: 70000 square km
""".strip()


def main():
    """Entry"""
    print()
    print("ORIGINAL DOCUMENT:")
    print(DOCUMENT)
    print()

    new_document = re.sub(r"\d+", format_with_comma, DOCUMENT)
    print("FORMATTED DOCUMENT:")
    print(new_document)
    print()


if __name__ == "__main__":
    main()
