#!/usr/bin/env python
"""
Adding values to a const is not a common operation
"""

import const


def main():
    """Entry"""
    color = const.define(red="0xff0000", green="0x00ff00", blue="0x0000ff")
    print("\n--- The constant")
    print(f"    {color}")

    print("\n--- Adding new constants")
    color = const.add(color, salmon="0xfa8072", plum="0xdda0dd")
    print(f"    {color}")

    print("\n--- Adding duplicates")
    try:
        color = const.add(color, salmon="grilled", plum="sweet", coral="0xff7f50")
    except ValueError as exc:
        print(f"    Error: {exc}")


if __name__ == "__main__":
    main()
