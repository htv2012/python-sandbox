#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config


def main():
    logging.config.fileConfig('default.ini')
    logger = logging.getLogger('default_logger')
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
