import itertools
import logging

import pytest


@pytest.fixture(scope="session")
def get_port():
    logging.warning("get_port fixture is called")
    ports_pool = itertools.count(10001)

    def get_next():
        return next(ports_pool)

    return get_next


@pytest.fixture(scope="session")
def get_ports_range():
    logging.warning("get_ports_range fixture is called")
    ports_pool = itertools.count(20001)

    def get_next(size=3):
        ports_list = [next(ports_pool) for _ in range(size)]
        start_value = ports_list[0]
        end_value = ports_list[-1]

        return f"{start_value}-{end_value}"

    return get_next
