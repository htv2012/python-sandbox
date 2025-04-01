#!/usr/bin/env python
import argparse
import logging
import os
import string

CAPS = string.ascii_uppercase
logging.basicConfig(level=os.getenv("LOGLEVEL", logging.WARN))
logger = logging.getLogger(__name__)


def camel_to_snake(camel):
    logger.debug("Name = %r", camel)

    def surrounded_by_caps(prevc, nextc):
        return prevc in CAPS and nextc in CAPS

    def convert(prevc, c, nextc):
        if c in CAPS and not surrounded_by_caps(prevc, nextc):
            c = "_" + c
        return c.lower()

    snake = "".join(
        convert(prevc, c, nextc)
        for prevc, c, nextc in zip("X" + camel, camel, camel[1:] + "X")
    )
    snake = snake.strip("_")
    return snake


def tryout(camel):
    snake = camel_to_snake(camel)
    print("{} ==> {}".format(camel, snake))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("camels", nargs="+")
    options = parser.parse_args()
    for camel in options.camels:
        tryout(camel)
