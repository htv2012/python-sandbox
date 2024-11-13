#!/usr/bin/env python3
"""
whatis: Custom exception with extra field
"""
class RecordError(Exception):
    def __init__(self, message, record=None):
        super().__init__(message)
        self.record = record


try:
    raise RecordError("Record not found", 51)
except RecordError as exc:
    print(exc)
    print(f"Record ID: {exc.record}")
