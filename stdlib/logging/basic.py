#!/usr/bin/env python3
"""
Demo a basic and easy way to use the logging library
Created by Hai Vu on 2012-10-18
"""
import logging


def main():
    # Configure a root logger with handlers and a standard formatter
    logging.basicConfig()

    # Create a new logger and configure
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Log away
    logger.debug('this is debug')
    logger.info('this is info')
    logger.warning('this is warning')
    logger.error('this is error')
    logger.critical('this is critical')


if __name__ == '__main__':
	main()
