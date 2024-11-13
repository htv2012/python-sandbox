# test_code.py
import logging


def test_a(data, c_value):
    logging.debug("data=%r", data)
    logging.debug("c_value=%r", c_value)


def test_b(data, c_value, d_value):
    logging.debug("data=%r", data)
    logging.debug("c_value=%r", c_value)
    logging.debug("d_value=%r", d_value)


def test_c():
    """This test do not use data."""
    pass
