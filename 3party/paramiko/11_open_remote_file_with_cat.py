#!/usr/bin/env python3
"""
Opens and reads a remote file
"""
import sshtools


def main():
    """Entry"""
    with sshtools.connect_with_config("nuc") as connection:
        _, stdout, _ = connection.exec_command("cat /etc/os-release")
        contents = stdout.read()
        contents = contents.decode("utf-8")
        print(contents)


if __name__ == "__main__":
    main()
