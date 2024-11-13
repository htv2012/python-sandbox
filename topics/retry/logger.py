#!/usr/bin/env python3
import logging
import os


logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
logger = logging.getLogger(__name__)

critical = logger.critical
debug = logger.debug
error = logger.error
fatal = logger.fatal
info = logger.info
warn = logger.warn
warning = logger.warning
