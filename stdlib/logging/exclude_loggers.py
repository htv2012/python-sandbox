#!/usr/bin/env python3
"""
Plays with logging filter
"""

import logging


class ExclusionFilter:
    """Filter out those log with certain names and levels."""
    def __init__(self, names, level=logging.DEBUG):
        self.names = names
        self.level = level

    def filter(self, record):
        if record.name in self.names:
            return False
        if self.level is not None and record.levelno < self.level:
            return False
        return True


def main():
    pass


handler = logging.StreamHandler()
handler.addFilter(ExclusionFilter(names=["foo", "bar"], level=logging.WARNING))
logger = logging.getLogger("sandbox")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info("Hello")
logger.error("Out of milk")

if __name__ == "__main__":
    main()
