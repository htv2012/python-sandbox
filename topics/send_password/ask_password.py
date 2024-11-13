#!/usr/bin/env python3

import getpass


def main():
    """Entry"""
    password = getpass.getpass("Enter password: ")
    if password == "hello":
        print("Correct")
    else:
        print("Incorrect")


if __name__ == "__main__":
    main()
