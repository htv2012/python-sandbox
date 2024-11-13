#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

config = {
    'version': 1,
    'loggers': {
        'default_logger': {
            'handlers': ['consoleHandler'],
            'level': 'DEBUG'
        },
    },
    'handlers': {
        'consoleHandler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'brief',
        },
    },
    'formatters': {
        'brief': {
            'format': '%(levelname)8s %(message)s',
        }
    },
}


def main():
    # logging.config.fileConfig('default.ini')
    logging.config.dictConfig(config)
    logger = logging.getLogger('default_logger')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
