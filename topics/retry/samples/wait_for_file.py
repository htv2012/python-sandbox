#!/usr/bin/env python3
import contextlib
import pathlib
import threading
import time

import flow
import logger

FILENAME = pathlib.Path("/tmp/deleteme.txt")


def create_file(file_name):
    logger.info("Waiting for a while")
    time.sleep(9)
    with open(file_name, "w") as f:
        f.write("Success")
    logger.info("File created")


def main():
    with contextlib.suppress(FileNotFoundError):
        FILENAME.unlink()

    threading.Thread(
        target=create_file,
        args=(FILENAME,),
    ).start()

    result = flow.retry(
        action=lambda: FILENAME.exists(),
        expect=True,
        logger=logger,
    )

    logger.info(f"Result: {result}")


if __name__ == "__main__":
    main()
