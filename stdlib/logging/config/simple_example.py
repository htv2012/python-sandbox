#!/usr/bin/env python3
import logging
import logging.config
import pathlib


def main():
    config_file = pathlib.Path(__file__).with_name('logging.ini')
    logging.config.fileConfig(config_file)
    logger = logging.getLogger('simpleExample2')
    logger.debug('debug message')
    logger.info('info message: %r', __name__)
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
