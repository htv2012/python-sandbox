#!/usr/bin/env python3
# conftest.py
import types

import pytest
import yaml


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--test-data-files",
        nargs="*",
        action="store",
        default=["default.yaml"],
        help="Data for parametrization",
    )


def _load_test_cases(test_data_files: list[str]):
    """
    Given a list of YAML data files, load them and create test cases data.
    """
    for filename in test_data_files:
        with open(filename, "r", encoding="utf-8") as stream:
            test_cases = yaml.safe_load(stream)
            for test_id, test_case in test_cases.items():
                param = pytest.param(types.SimpleNamespace(**test_case), id=test_id)
                yield param


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "test_data" in metafunc.fixturenames:
        test_data_files = metafunc.config.getoption("test_data_files")
        metafunc.parametrize(
            "test_data", _load_test_cases(test_data_files), scope="session"
        )
