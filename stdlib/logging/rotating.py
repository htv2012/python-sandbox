#!/usr/bin/env python
# encoding: utf-8
"""
rotating.py
Created by Hai Vu on 2010-07-10.
"""

import glob
import logging
import logging.handlers


def main():
    LOG_FILENAME = '/tmp/logging_rotating.log'
    my_logger = logging.getLogger('logging_rotating')
    my_logger.setLevel(logging.DEBUG)

    handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME,
        maxBytes=100,
        backupCount=5)
    my_logger.addHandler(handler)

    # Start logging
    for i in range(1000):
        my_logger.debug('i = %d' % i)
    logfiles = glob.glob('%s*' % LOG_FILENAME)
    for filename in logfiles:
        print(filename)
        print((open(filename).read()))
        print()

if __name__ == '__main__':
    main()
