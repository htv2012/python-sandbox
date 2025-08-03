import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def __getattr__(name):
    return getattr(logger, name)
