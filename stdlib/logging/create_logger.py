#!/usr/bin/env python

import logging
import logging.handlers

'''
Log both to a file and to console: use 2 different handlers

Logging:
  http://docs.python.org/2/library/logging.html

Formatter:
  http://docs.python.org/2/library/logging.html#logrecord-attributes

'''


def create_logger(logger_name, log_level=logging.WARNING, filename=None, format_str=None):
    '''
    Create a logger that log to the console, if a filename is supplied, log to that file
    as well.
    '''
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # create console handler and set appropriate level
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter(format_str or "%(asctime)s %(name)s %(levelname)-8s %(message)s")
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


def main():
    log_filename = 'logs/create_logger.log'
    logger = create_logger('demo', logging.DEBUG, log_filename)

    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")

    # Show the log file contents
    print('---')
    print(log_filename)
    print('---')
    with open(log_filename) as f:
        print(f.read())

if __name__ == '__main__':
    main()
