#!/usr/bin/env python3
"""
Demo: How to feed password to the sudo command.
"""
import getpass
import subprocess


def main():
    """Entry"""
    password = getpass.getpass("Enter password for sudo: ")
    process = subprocess.run(
        ["sudo", "-S", "ls", "/tmp"],
        encoding="utf-8",
        input=password,
        capture_output=True,
        check=True,
    )
    print(process.stdout)


if __name__ == "__main__":
    main()
