#!/usr/bin/env python3
import logging

# We trust that someone configured the logging system already

logger = logging.getLogger("mylib")
logger.debug("A debug message from mylib")
logger.info("Hello, world")
