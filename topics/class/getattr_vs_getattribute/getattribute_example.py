#!/usr/bin/env python
"""
__getattribute__ always get called regardless if the attribute is present
or not. Developers must exercise care not to get into endless recursion
trying to access an attribute.
"""

import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MyThing(object):
    def __init__(self):
        self.a = "prop a"

    def __getattribute__(self, name):
        try:
            attribute = super(MyThing, self).__getattribute__(name)
            return attribute
        except AttributeError as e:
            if name == "b":
                return "b prop"
            raise


if __name__ == "__main__":
    mything = MyThing()

    # Look up OK, __getattr__ not called
    logger.info("a is %r", mything.a)

    logger.info("b is %r", mything.b)

    logger.info("Attempt to get c")
    try:
        logger.info("c is %r", mything.c)
    except AttributeError as e:
        logger.error(e)
