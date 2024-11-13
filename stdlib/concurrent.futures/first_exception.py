#!/usr/bin/env python3
"""
Stops by first exception or when all is done.
Inspired by: https://stackoverflow.com/q/79039069/459745
"""

import logging
import logging.config
import pathlib
import sys
from concurrent.futures import FIRST_EXCEPTION, ThreadPoolExecutor, wait

logging.config.fileConfig(pathlib.Path(__file__).with_name("logging.ini"))


def divy(numerator: float, denominator: float):
    logging.debug("numerator=%r", numerator)
    logging.debug("denominator=%r", denominator)
    return numerator / denominator


def main():
    data = [
        (35.0, 7.0),
        (45.0, 8.0),
        (32.0, 0.0),
        (42.0, 3.3),
        (7.0, 1.5),
    ]
    with ThreadPoolExecutor() as executor:
        fs = {executor.submit(divy, *datum): datum for datum in data}
        results = wait(fs, return_when=FIRST_EXCEPTION)

    print("\nNot Done:")
    for future in results.not_done:
        print("%.1f / %.1f" % fs[future])

    print("\nDone:")
    for future in results.done:
        print("%.1f / %.1f = " % fs[future], end="")
        sys.stdout.flush()
        print("%.1f" % future.result())  # Might trigger an exception


if __name__ == "__main__":
    main()
