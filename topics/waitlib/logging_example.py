#!/usr/bin/env python3
import logging

logging.basicConfig(level="DEBUG")
main_logger = logging.getLogger("main_logger")
main_logger.debug("from main_logger")

muted_logger = logging.getLogger("muted_logger")
muted_logger.debug("before muting")
muted_logger.setLevel(logging.WARNING)

# Why do I still see this output?
muted_logger.debug("after muting, should not see this")
muted_logger.warning("Out of coffee")
