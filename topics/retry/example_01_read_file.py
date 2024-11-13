#!/usr/bin/env python3
"""
Demonstrate the use of the retry function

1. Create a separate thread to create a file after a short delay
2. In the main thread, try to read that file until success or timed out
"""
import contextlib
import os
import threading
import time

import flow
import logger


FILENAME = "/tmp/foo"


def create_file_after_delay():
    """
    Creates the contents of a file after some delay
    """
    logger.info("Sleep before creating file")
    time.sleep(9)

    logger.info("Create contents")
    with open(FILENAME, "w") as stream:
        stream.write("Demo Succeeded")


def main():
    """
    Main Entry
    """
    with contextlib.suppress(FileNotFoundError):
        os.unlink(FILENAME)

    thread = threading.Thread(target=create_file_after_delay)
    thread.start()

    contents = flow.retry(action=lambda: open(FILENAME).read())
    print(contents)


if __name__ == "__main__":
    main()
