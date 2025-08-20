import logging
import logging.handlers
import queue

QUEUE = queue.Queue()

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.addHandler(logging.handlers.QueueHandler(QUEUE))

info = LOGGER.info
