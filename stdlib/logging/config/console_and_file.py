#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config


def main():
    logging.config.fileConfig('logging.ini')
    logger = logging.getLogger('consoleAndFile')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
