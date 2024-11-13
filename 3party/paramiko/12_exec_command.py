#!/usr/bin/env python3
"""
Opens and reads a remote file
"""
import sshtools


def main():
    """Entry"""
    with sshtools.connect_with_config("nuc") as connection:
        _, stdout, stderr = connection.exec_command("lsb_release --all")
        contents = stdout.read()
        contents = contents.decode("utf-8")
        print(contents)

        error = stderr.read()
        if error:
            error = error.decode("utf-8")
            print("\nERROR:")
            print(error)


if __name__ == "__main__":
    main()
