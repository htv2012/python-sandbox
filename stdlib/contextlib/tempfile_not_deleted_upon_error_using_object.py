#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Pattern: Create a temp file, but only delete it when test passed """

import logging
import os
import unittest
import tempfile


logger = logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s:%(funcName)s:%(lineno)d:%(message)s',
    )


class TempFile(object):
    def __init__(self, mode='w+b', **kwargs):
        # Overwrite the 'delete' paramter
        kwargs['delete'] = False

        self.file_object = tempfile.NamedTemporaryFile(mode=mode, **kwargs)
        logging.debug('TempFile: filename = %s', self.file_object.name)

    def __enter__(self):
        return self.file_object

    def __exit__(self, exception_type, exception_value, traceback):
        if any((exception_type, exception_value, traceback)):
            logging.error('TempFile: An error occurred, will not delete temp file %s', self.file_object.name)
        else:
            logging.debug('TempFile: delete %s', self.file_object.name)
            self.file_object.close()
            os.unlink(self.file_object.name)
        return False  # Do not suppress exception


class MyTests(unittest.TestCase):
    def test_that_failed(self):
        with TempFile(prefix='abcd_', suffix='.txt') as file_object:
            file_object.write('Test that fail')
            self.fail('Test meant to be failing')

    def test_that_passed(self):
        with TempFile() as file_object:
            file_object.write('Hello')

if __name__ == '__main__':
    unittest.main()
