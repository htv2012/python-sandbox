"""
stuff.py
"""
import logging

import config


def perform():
    logger = logging.getLogger("config.stuff")
    logger.info(f"Config in perform: {config.name}")


if __name__ == '__main__':
    pass
