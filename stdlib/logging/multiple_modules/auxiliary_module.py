import logging
# from setup_logger import logger

# create logger
logger = logging.getLogger('spam.aux')
logger.info('xyz module start')

class Auxiliary(object):
    def __init__(self):
        self.logger = logging.getLogger('spam.aux.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    logger.info('received a call to "some_function"')
