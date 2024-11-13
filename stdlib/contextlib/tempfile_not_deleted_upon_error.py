#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Pattern: Create a temp file, but only delete it when test passed """

import os
import contextlib
import logging
import unittest
import tempfile

logging.basicConfig(level=logging.DEBUG)


@contextlib.contextmanager
def create_temp_file(mode='wb'):
    try:
        handle, filename = tempfile.mkstemp()
        logging.debug('create_temp_file: handle, filename = %d, %s', handle, filename)
        os.close(handle)
        tempf = open(filename, mode)
        yield tempf
    except Exception:
        logging.error('create_temp_file: An error occurred, will not delete temp file %s', filename)
        raise
    finally:
        tempf.flush()
        tempf.close()

    # Only delete the file if no error
    logging.debug('create_temp_file: deleting file %s', filename)
    os.remove(filename)



class MyTests(unittest.TestCase):
    def setUp(self):
        logging.info('Start %s', self.id().split('.')[-1])

    def tearDown(self):
        logging.info('End test')

    def test_that_failed(self):
        with create_temp_file() as tempf:
            tempf.write('Start test')
            tempf.write('Value of X: {}'.format(x))

    def test_that_passed(self):
        x = 5
        with create_temp_file() as tempf:
            tempf.write('Start test')
            tempf.write('Value of X: {}'.format(x))

if __name__ == '__main__':
    unittest.main()
