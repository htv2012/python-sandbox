#!/usr/bin/env python3
"""
Upload a file
"""
import contextlib

import sshtools


def main():
    """Entry"""
    client = sshtools.connect_with_config("nuc")
    remote_dir = "/tmp/nothing_in_here"
    with client.open_sftp() as sftp:
        print("Delete existing dir, ignore error")
        with contextlib.suppress(OSError):
            sftp.rmdir(remote_dir)

        print("Mkdir, should not error")
        sftp.mkdir(remote_dir)

        print("Mkdir again")
        try:
            sftp.mkdir(remote_dir)
        except OSError:
            print("Error, cannot do that")


if __name__ == "__main__":
    main()
