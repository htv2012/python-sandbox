"""Show what the framework passes to a scope function."""

import logging
from typing import Literal

import pytest


def scope_func(
    fixture_name: str, config: pytest.Config
) -> Literal["session", "package", "module", "function"]:
    logging.info("A scope fuction takes in the following parameters:")
    logging.info(
        "- fixture_name: %s = %r", fixture_name.__class__.__name__, fixture_name
    )
    logging.info("- config: %s = %r", config.__class__.__name__, config)
    return "function"


@pytest.fixture(scope=scope_func)
def test_it():
    pass
