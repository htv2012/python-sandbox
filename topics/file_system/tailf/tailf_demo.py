#!/usr/bin/env python3
import atexit
from concurrent.futures import ThreadPoolExecutor
import os
import tempfile
import pathlib
import time

import tailf


def read_contents(path):
    """"Read continuously from a file and displays the lines."""
    print("read started")
    for line in tailf.tailf(path):
        print(line, end="", flush=True)
    print("read end")


def write_contents(path):
    for number in range(20):
        with open(path, "a") as stream:
            stream.write(f"Hello {number}\n")
        time.sleep(1)


def main():
    """ Entry """
    # Get path to a unique temp file name and schedule deletion
    temp_path = pathlib.Path(tempfile.mktemp())
    print(f"Path: {temp_path}")
    atexit.register(temp_path.unlink, missing_ok=True)

    with ThreadPoolExecutor() as executor:
        read_thread = executor.submit(read_contents, temp_path)
        write_contents(temp_path)
        # write_thread = executor.submit(write_contents, temp_path)
        read_thread.cancel()
    

if __name__ == '__main__':
    main()
