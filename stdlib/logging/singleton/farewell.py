#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('mylogger.farewell')
logger.debug('Enter farewell')


def bye():
    logger.info('Goodbye')


logger.debug('Exit farewell')
