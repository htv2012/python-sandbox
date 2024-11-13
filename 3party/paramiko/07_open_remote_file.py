#!/usr/bin/env python3
"""
Opens and reads a remote file
"""
import sshtools


def main():
    """Entry"""
    with (
        sshtools.connect_with_config("nuc") as connection,
        connection.open_sftp() as sftp,
        sftp.file("/etc/os-release") as file,
    ):
        contents = file.read()
        contents = contents.decode("utf-8")
        print(contents)


if __name__ == "__main__":
    main()
