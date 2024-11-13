import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('mymodule')

logger.debug('start')

def greet(name):
    logger.debug('Name is %s', name)
    print('Hello, {}'.format(name))
