"""Show what inside an item."""

import logging

import introspect
import pytest


def pytest_collection_modifyitems(
    session: pytest.Session, config: pytest.Config, items: list[pytest.Item]
):
    logging.info("Show what inside a pytest.Item")
    introspect.explore(items[0], "items[0]")
