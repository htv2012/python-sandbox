#!/usr/bin/env python
import logging


INFO = logging.INFO
DEBUG = logging.DEBUG
WARNING = logging.WARNING


class SelectiveLabelsHandler(logging.StreamHandler):
    def __init__(self, formatstr=logging.BASIC_FORMAT, filter=None):
        formatter = logging.Formatter(formatstr)
        self.setFormatter(formatter)
        if filter is None:
            filter = lambda rec: True
        self._filter = filter

    def handle(self, record):
        if self._filter(record):
            self.emit(record)


def create_logger(logger_name, log_level=logging.WARNING, filename=None):
    """ Create a logger that log to the console, if a filename is
    supplied, log to that file as well.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # create console handler and set appropriate level
    # ch = logging.StreamHandler()
    ch = SelectiveLabelsHandler(filter=lambda r: r.levelno <= logging.INFO)
    logger.addHandler(ch)

    # ch = SelectiveLabelsHandler(filter=lambda r: r.levelno > logging.INFO)
    # logger.addHandler(ch)

    # Create a file handler and set appropriate level
    if filename:
        fh = logging.FileHandler(filename=filename, mode='w')
        fformatter = logging.Formatter(
            '%(asctime)s;%(filename)s;%(lineno)d;%(levelname)s;%(message)s',
            "%Y-%m-%d %H:%M:%S")
        fh.setFormatter(fformatter)
        logger.addHandler(fh)
    return logger

logger = create_logger('labels', log_level=DEBUG)
logger.info('hello, world')
logger.debug('pull my finger')
logger.warning('File not found, create one with defaults')
