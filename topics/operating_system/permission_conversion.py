#!/usr/bin/env python
import argparse
import subprocess

def rwx_to_octal(rwx):
    result = \
            (0b100 if 'r' in rwx else 0) + \
            (0b010 if 'w' in rwx else 0) + \
            (0b001 if 'x' in rwx else 0)
    return f"{result:o}"


def permission_to_octal(permission):
    return rwx_to_octal(permission[1:4]) + rwx_to_octal(permission[4:7]) + rwx_to_octal(permission[7:10])


def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument("dirname", nargs="+")
    options = parser.parse_args()

    for dirname in options.dirname:
        print(f"\n{dirname}")

        output = subprocess.check_output(["/bin/ls", "-l", dirname], encoding="utf-8")
        for line in output.splitlines()[1:]:
            permission = line.split()[0]
            octal = permission_to_octal(permission)
            print(f"{octal} {line}")


if __name__ == '__main__':
    main()
