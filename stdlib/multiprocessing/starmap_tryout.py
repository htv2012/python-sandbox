#!/usr/bin/env python3
"""
Try starmap
"""

import logging
import logging.config
import multiprocessing
import pathlib
import random
import time

logging.config.fileConfig(pathlib.Path(__file__).with_name("logging.ini"))


def adder(a, b):
    logging.debug("Enter adder, a=%r, b=%r", a, b)
    time.sleep(random.randint(1, 3))
    result = a + b
    return result


def main():
    logging.info("Start")
    with multiprocessing.Pool() as pool:
        results = pool.starmap(adder, [(1, 2), (3, 4)])
        for result in results:
            logging.info("result=%r", result)
    logging.info("End")


if __name__ == "__main__":
    main()
