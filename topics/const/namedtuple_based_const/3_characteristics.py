#!/usr/bin/env python
"""
Characteristics of a const
"""
import const


def main():
    """Entry"""
    color = const.define(red="0xff0000", green="0x00ff00", blue="0x0000ff")
    print("\n--- The constant")
    print(f"    {color}")

    print("\n--- First value")
    print(f"    {color[0]}")

    print("\n--- Last value")
    print(f"    {color[-1]}")

    print("\n--- Membership testing")
    result = "0xffffff" in color
    print(f"    0xffffff in the color? {result}")

    result = "0xff0000" in color
    print(f"    0xff0000 in color? {result}")

    print("\n--- Iterating")
    for value in color:
        print(f"    {value}")

    print("\n--- Creating a dictionary")
    print(f"    {color._asdict()}")


if __name__ == "__main__":
    main()
