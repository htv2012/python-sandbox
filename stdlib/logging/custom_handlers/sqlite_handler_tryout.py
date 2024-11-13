#!/usr/bin/env python
import logging
import os

from custom_handlers import SQLiteHandler


if __name__ == '__main__':
    # Create a new logger with overall level set to DEBUG, however, each
    # individual handler can set its own level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    script_dir = os.path.dirname(__file__)
    log_filename = os.path.join(script_dir, 'logoutput.sqlite')

    sqlite_handler = SQLiteHandler(log_filename)
    logger.addHandler(sqlite_handler)

    # Start logging
    logger.error('This is error')
    logger.warn('This is warn')
    logger.info('This is info')
    logger.debug('This is %s', 'debug')
