#!/usr/bin/env python3
import tabulate

TABLE = [(501, "johnk", "bash"), (502, "karenc", "tcsh")]

HEADERS = ("User ID", "alias", "shell")


def try_style(style):
    print()
    print("-" * 80)
    print(f"Style: {style}")
    print("-" * 80)
    print(tabulate.tabulate(TABLE, headers=HEADERS, tablefmt=style))


def main():
    """Entry"""
    styles = [None] + sorted(tabulate.tabulate_formats)
    for style in styles:
        try_style(style)


if __name__ == "__main__":
    main()
