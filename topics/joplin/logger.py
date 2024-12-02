#!/usr/bin/env python3
"""
Common log object
"""

import logging
import os

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "WARNING"),
    format="%(levelname)-12s | %(message)s",
)

debug = logging.debug
info = logging.info


