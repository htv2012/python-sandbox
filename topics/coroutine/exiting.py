#!/usr/bin/env python
"""
DEMO: How to close or raise exception in coroutine
"""
from coroutine import coroutine
import logging

format = '%(funcName)-16s | %(message)s' 
logging.basicConfig(level=logging.DEBUG, format=format)
logger = logging.getLogger(__name__)


@coroutine
def simple_coroutine():
    logger.info('Setting up the coroutine')
    try:
        while True:
            logger.info('Waiting for item')
            item = yield
            logger.info('Got item: %r' % item)
    except GeneratorExit:
        logger.info('Normal exit')
    finally:
        logger.info('Finally')


def main():
    """ Entry """
    logger.info('main starts')
    active_coroutine = simple_coroutine()
    active_coroutine.send('green eggs')
    active_coroutine.send('spam')
    active_coroutine.close()
    logger.info('main ends')


if __name__ == '__main__':
    main()
