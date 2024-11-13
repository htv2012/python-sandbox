#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .mylogger import logger
from .greet import hello
from .farewell import bye


if __name__ == '__main__':
    logger.info('Start main')
    hello('world')
    bye()
    logger.info('End main')
