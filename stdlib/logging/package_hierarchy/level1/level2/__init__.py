import logging

logger = logging.getLogger(__name__)
logger.info('Initialize level2')


def greet(name):
    logger.debug('Enter greet(name=%r)', name)
