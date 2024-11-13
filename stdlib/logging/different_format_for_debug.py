"""
whatis: How to create a logging object which has different formatting for debug?
"""
import logging


class DebugOnly(logging.Filter):
    """ This filter only accept records with debug level """
    def filter(self, record):
        return record.levelno == logging.DEBUG


if __name__ == '__main__':
    # Create a new logger with overall level set to DEBUG, however, each
    # individual handler can set its own level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # The debug handler, which only handle debug level and has its own formatter
    debug_handler = logging.StreamHandler()
    debug_handler.addFilter(DebugOnly())
    debug_handler.setFormatter(logging.Formatter('==> %(message)s'))
    logger.addHandler(debug_handler)

    # The regular handler, which only handles info level and higher. That means
    # it will not handle records with debug level
    non_debug_handler = logging.StreamHandler()
    non_debug_handler.setLevel(logging.INFO)
    logger.addHandler(non_debug_handler)

    # Start logging
    logger.error('This is error')
    logger.warn('This is warn')
    logger.info('This is info')
    logger.debug('This is debug')
