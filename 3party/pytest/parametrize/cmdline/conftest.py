#!/usr/bin/env python3
# conftest.py
# stackoverflow url: https://stackoverflow.com/q/78774245/459745
import json
import logging

import pytest

DATA_LIST = []


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--data",
        action="store",
        default="[[1, 2], [3, 4], [5, 6]]",
        help="Data for parametrization",
    )


def pytest_generate_tests(metafunc: pytest.Metafunc):
    global DATA_LIST

    # Only parametrize for the 'data' fixture
    if "data" not in metafunc.fixturenames:
        logging.debug("No data fixture in %s()", metafunc.definition.name)
        return

    # Using pytest.param() gives us the option
    # to assign an ID to the test data
    if not DATA_LIST:
        DATA_LIST = [
            pytest.param(data, id=f"a={data[0]}, b={data[1]}")
            for data in json.loads(metafunc.config.getoption("data"))
        ]
        logging.debug("DATA_LIST generated for %s():", metafunc.definition.name)
        for param in DATA_LIST:
            logging.debug("- %r", param)
    else:
        logging.debug("Using cached DATA_LIST for %s()", metafunc.definition.name)
    metafunc.parametrize("data", DATA_LIST, scope="session")


@pytest.fixture(scope="session")
def c_value(data):
    return sum(data)


@pytest.fixture(scope="session")
def d_value(c_value):
    return c_value * 2
