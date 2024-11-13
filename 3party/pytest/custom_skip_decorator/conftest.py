import os
import logging

import pytest


def pytest_runtest_setup(item):
    for mark in item.iter_markers(name="require_env"):
        logging.debug("mark=%r", mark)
        var_name = mark.args[0]
        if len(mark.args) >= 2:
            reason = mark.args[1]
        else:
            reason = f"Need to define {var_name}"
        if var_name not in os.environ:
            pytest.skip(reason)
