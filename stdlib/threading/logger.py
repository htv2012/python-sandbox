import logging
import os

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "DEBUG"),
    format="%(asctime)s %(levelname)-12s: %(threadName)-12s: %(message)s",
)

LOGGER = logging.getLogger()

critical = LOGGER.critical
debug = LOGGER.debug
error = LOGGER.error
exception = LOGGER.exception
info = LOGGER.info
warning = LOGGER.warning
