import logging
import logging.config
import os
import pathlib


config_path = pathlib.Path(__file__).with_name("logging.ini")
logging.config.fileConfig(config_path)
logger = logging.getLogger(__name__)

level = os.getenv("LOGLEVEL")
if level is not None:
    logger.setLevel(level)


critical = logging.critical
debug = logger.debug
error = logging.error
exception = logging.exception
info = logger.info
warning = logging.warning
