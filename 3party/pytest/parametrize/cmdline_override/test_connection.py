# test_code.py
import logging


def test_connection(test_data):
    logging.debug("test_data=%r", test_data)
    assert test_data.port > 999
