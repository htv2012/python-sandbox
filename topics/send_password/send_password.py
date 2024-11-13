#!/usr/bin/env python3

import pexpect


def main():
    """Entry"""
    child = pexpect.spawn("python ask_password.py")
    child.expect("Enter password: ")
    child.sendline("hello")

    print(child.read())


if __name__ == "__main__":
    main()
