"""
We can affect someone else's logger. For example, set the level
"""
import logging

GARBAGE = logging.getLogger('mymodule')
GARBAGE.setLevel(logging.WARN)
import mymodule

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('main')

logger.debug('start')
mymodule.greet('world')
