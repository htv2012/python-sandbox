#!/usr/bin/env python3
import logging

logger = logging.getLogger("mylib.util")
logger.setLevel(logging.DEBUG)


def calculate_key(a, b):
    key = a + b
    logger.debug("a=%r, b=%r, key=%r", a, b, key)
    return key
