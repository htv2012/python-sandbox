#!/usr/bin/env python
"""
Logging tools to be used with unittest
"""

from functools import wraps
import logging

INFO = logging.INFO
DEBUG = logging.DEBUG
WARNING = logging.WARNING


def create_logger(logger_name, log_level=logging.WARNING, filename=None):
    """ Create a logger that log to the console, if a filename is
    supplied, log to that file as well.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # create console handler and set appropriate level
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)-8s %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Create a file handler and set appropriate level
    if filename:
        fh = logging.FileHandler(filename=filename, mode='w')
        fh.setLevel(log_level)
        fformatter = logging.Formatter(
            '%(asctime)s;%(filename)s;%(lineno)d;%(levelname)s;%(message)s',
            "%Y-%m-%d %H:%M:%S")
        fh.setFormatter(fformatter)
        logger.addHandler(fh)
    return logger

def test_case_logger(logger=None):
    """ A decorator for unittest.TestCase which adds logging prologue
    and epilogue for each test cases.
    :param logger: The logger object, if None, then a default logger is
    used.
    """
    if logger is None:
        logger = create_logger(__name__, log_level=logging.DEBUG)

    def add_logging(cls):
        original_setup = getattr(cls, 'setUp')
        original_teardown = getattr(cls, 'tearDown')
        test_id = getattr(cls, 'id')

        # Add logging for each test's prologue
        @wraps(original_setup)
        def setUp_with_logging(test_instance, *args, **kwargs):
            logger.debug('============================================')
            logger.info('Enter test %s', test_id(test_instance))
            original_setup(test_instance, *args, **kwargs)

        # Add logging for each test's epilogue
        @wraps(original_teardown)
        def tearDown_with_logging(test_instance, *args, **kwargs):
            original_teardown(test_instance, *args, **kwargs)
            logger.info('Exit test %s', test_id(test_instance))

        # Replace the original setUp and tearDown with those that add
        # logging
        setattr(cls, 'setUp', setUp_with_logging)
        setattr(cls, 'tearDown', tearDown_with_logging)
        return cls

    return add_logging

