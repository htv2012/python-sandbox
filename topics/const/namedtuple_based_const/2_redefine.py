#!/usr/bin/env python
"""
Example of how to use the const package
"""
import const


def main():
    """Entry"""
    color = const.define(red="0xff0000", green="0x00ff00", blue="0x0000ff")
    print(f"color: {color}")
    print(f"green: {color.green}")

    print("Attempt to redefine green")
    try:
        color.green = "0xffffff"
    except AttributeError:
        print("Cannot do it")
    print(f"green is now: {color.green}")


if __name__ == "__main__":
    main()
