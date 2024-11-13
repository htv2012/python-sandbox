# mod2.py
import logging
import setup_logger

# mod2 creates its own logger, as a sub logger to 'spam'
logger = logging.getLogger('spam.mod2')

class Class2:
    def do_something(self):
        logger.info('Class2: doing something')
