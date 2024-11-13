#!/usr/bin/env python3
"""
See which order the clean ups take place
"""
import contextlib
import logging


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


@contextlib.contextmanager
def context1():
    LOGGER.info("context1 starts")
    yield
    LOGGER.info("context1 ends")


@contextlib.contextmanager
def context2():
    LOGGER.info("context2 starts")
    yield
    LOGGER.info("context2 ends")




def main():
    """ Entry """
    with context1(), context2():
        LOGGER.info("In the with statement")


if __name__ == "__main__":
    main()

