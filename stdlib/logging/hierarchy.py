#!/usr/bin/env python3
"""
Demo child loggers which inherit parent's attributes
Created by Hai Vu on 2012-10-18.
"""
import logging


def child1():
    logger = logging.getLogger('main.child1')
    logger.info('this is info')
    logger.debug('this is debug')


def main():
    logging.basicConfig()
    logger = logging.getLogger('main')

    # Set level to INFO, affect both main and child1
    logger.setLevel(logging.INFO)
    logger.info('this is an info line')
    logger.debug('this is a debug line')
    child1()

    # Set level to DEBUG, affect both main and child1
    logger.setLevel(logging.DEBUG)
    logger.info('this is an info line')
    logger.debug('this is a debug line')
    child1()

    child_logger = logging.getLogger('main.child1')
    assert child_logger.parent is logger


if __name__ == '__main__':
    main()
