#!/usr/bin/env python
# encoding: utf-8
"""
logging_minimal.py

Created by Hai Vu on 2013-05-04.
Copyright (c) 2013 High View Software. All rights reserved.
"""

import sys
import os
import logging

def main():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('this is a debug line')
    logging.info('info line')
    logging.warning('warning line')

if __name__ == '__main__':
    main()

