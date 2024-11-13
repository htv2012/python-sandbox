#!/usr/bin/env python
"""
__getattr__ get called after looking up an attribute failed
"""

import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MyThing(object):
    a = "a attribute"

    def __getattr__(self, name):
        logger.debug("__getattr__ called with %r", name)
        if name == "b":
            return "b attribute"

        error_message = "{!r} object has not attribute {!r}".format(
            self.__class__.__name__, name
        )
        raise AttributeError(error_message)


if __name__ == "__main__":
    mything = MyThing()

    # Look up OK, __getattr__ not called
    logger.info("a is %r", mything.a)

    logger.info("b is %r", mything.b)
    try:
        logger.info("c is %r", mything.c)
    except AttributeError as e:
        logger.error(e)
