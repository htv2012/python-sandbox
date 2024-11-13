#!/usr/bin/env python3
from logger import logger

import yaml

from mylib import util


def main():
    """ Entry """
    key = util.calculate_key("abc", "123")
    logger.info("Key: %r", key)


if __name__ == '__main__':
    main()
