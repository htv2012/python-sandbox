#!/usr/bin/env python3
"""
Parses the output of the df command
"""
import collections
import csv
import io
import os
import subprocess

DfEntry = collections.namedtuple(
    "DfEntry",
    "filesystem size used available percent_used mounted_on",
)


def get_disk_free_output():
    command = ["df", "-P"]
    output = subprocess.getoutput(command)
    return output


def _str2int(s):
    try:
        return int(s)
    except ValueError:
        return s

def _make_entry(tup):
    values = [_str2int(value) for value in tup]
    return DfEntry(*values)


def parse_disk_free_output(text):
    """
    Parses the output of `df -P` command such as

    Filesystem                            1024-blocks         Used    Available Capacity Mounted on
    devtmpfs                                  1928372            0      1928372       0% /dev
    tmpfs                                     1940136            0      1940136       0% /dev/shm

    ... and returns a list of DfEntry:

    [
        DfEntry(filesystem='devtmpfs', size=1928372, used=0, available=1928372, percent_used=0, mounted_on='/dev'),
        DfEntry(filesystem='tmpfs', size=1940136, used=0, available=1940136, percent_used=0, mounted_on='/dev/shm')
    ]    

    """
    lines = iter(text.replace("%", "").splitlines())
    next(lines)  # Remove the header line
    entries = [
        _make_entry(line.split())
        for line in lines
    ]
    return entries


def main():
    text = get_disk_free_output()
    entries = parse_disk_free_output(text)
    for entry in entries:
        print(entry)


if __name__ == "__main__":
    main()
