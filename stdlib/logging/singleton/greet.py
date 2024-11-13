#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .mylogger import logger

logger.debug('Enter greet')


def hello(name):
    logger.info('Hello %s', name)

logger.debug('Exit greet')
