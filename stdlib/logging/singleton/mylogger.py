#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module sets up the logger for use in the whole project
"""
import logging
import os


log_level = logging.INFO
if 'DEBUG' in os.environ:
    log_level = logging.DEBUG

logging.basicConfig(format='%(message)s', level=log_level)
logger = logging.getLogger(name='mylogger')
