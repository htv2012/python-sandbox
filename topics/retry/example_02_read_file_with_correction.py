#!/usr/bin/env python3
"""
Demonstrate the use of the correction

1. Create a separate thread to create a file after a short delay
2. In the main thread, try to read that file until success or timed out
"""
import contextlib
import os

import logger
import flow


def create_contents(file_name):
    """
    Creates the contents of a file after some delay
    """
    logger.info(f"create file {file_name}")
    with open(file_name, "w") as stream:
        stream.write("Demo Succeeded")


def main():
    """
    Main Entry
    """
    file_name = "/tmp/foo"

    with contextlib.suppress(FileNotFoundError):
        os.unlink(file_name)

    contents = flow.retry(
        action=lambda: open(file_name).read(),
        correction=lambda: create_contents(file_name),
        delay=1,
        logger=logger,
    )
    print(contents)


if __name__ == "__main__":
    main()
