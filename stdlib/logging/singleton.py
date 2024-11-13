#!/usr/bin/env python3
"""
whatis: Give the same name to getLogger and get the same object
"""
import logging

logging.basicConfig()

logger1 = logging.getLogger('foo')
logger2 = logging.getLogger('foo')

if logger1 is logger2:
    print('logger1 and logger2 are the same')
