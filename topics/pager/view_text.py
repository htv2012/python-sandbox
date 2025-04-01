#!/usr/bin/env python3
"""
Demo of view_text()
"""

import pager


def main():
    """Entry"""
    with open("lorem.txt", encoding="utf-8") as file_handle:
        text = file_handle.read()

    pager.view_text(text)
    print("\n\nHave a nice day.")


if __name__ == "__main__":
    main()
