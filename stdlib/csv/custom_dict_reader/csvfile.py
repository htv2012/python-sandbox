#!/usr/bin/env python

import contextlib
import csv
import functools


# class ListReader(object):
#     def __init__(self, file_object, mode='r', reader=csv.reader):
#         if hasattr(file_object, 'read'):
#             self.file_handle = file_object
#         else:
#             self.file_handle = open(file_object)

#         self.csv_reader = reader(self.file_handle)

#     def __enter__(self):
#         return self.csv_reader

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file_handle.close()

# class DictReader(ListReader):
#     '''
#     DictReader is the same as Reader, except it employs csv.DictReader instead of the
#     default csv.reader.
#     '''
#     def __init__(self, file_object, mode='r'):
#         super(DictReader, self).__init__(file_object, mode, reader=csv.DictReader)

@contextlib.contextmanager
def DictReader(file_name):
    with open(file_name) as f:
        reader = csv.DictReader(f)
        yield reader


@contextlib.contextmanager
def list_reader(file_name, reader=csv.reader):
    with open(file_name) as f:
        reader = reader(f)
        yield reader

dict_reader = functools.partial(list_reader, reader=csv.DictReader)

