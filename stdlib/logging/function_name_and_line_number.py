#!/usr/bin/env python
"""
Demo: Create a logger which shows the file name, line number, and the
name of the function on the log line
"""

from create_logger import create_logger


logger = create_logger(
    'func_and_line',
    log_level='INFO',
    format_str='%(filename)s:%(lineno)d:%(funcName)s: %(message)s')


def hello(name):
    logger.info('Hello, %s', name)


def main():
    logger.info('logger created')
    hello('world')


if __name__ == '__main__':
    main()
