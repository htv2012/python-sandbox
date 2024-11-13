import logging

import pytest


@pytest.mark.Sunday
def test_m1_sunday():
    logging.debug("Beautiful Sunday")


@pytest.mark.Monday
def test_m1_monday():
    pass


@pytest.mark.Tuesday
def test_m1_tuesday():
    pass


@pytest.mark.Wednesday
def test_m1_wednesday():
    pass


@pytest.mark.Thursday
def test_m1_thursday():
    pass


@pytest.mark.Friday
def test_m1_friday():
    pass


@pytest.mark.Saturday
def test_m1_saturday():
    pass
