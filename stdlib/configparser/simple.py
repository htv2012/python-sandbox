#!/usr/bin/env python3
"""
A Python skeleton script
"""

from configparser import ConfigParser


def main():
    """Entry"""
    parser = ConfigParser()
    parser.read("data/simple.ini")

    print("\nShow selected fields:")
    print("version=%d" % parser.getint("product", "version"))
    print("commit=%s" % parser.get("product", "commit"))

    print("\nShow all fields in a section:")
    for key, value in parser.items("product"):
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
