#!/usr/bin/env python3
"""
Parameterize test
"""
import pathlib

import pytest
import yaml


@pytest.mark.parametrize(
    "input_value,expected", [(False, True), (1, True), ("abc", False)]
)
def test_is_int(input_value, expected):
    assert isinstance(input_value, int) == expected


@pytest.mark.parametrize("x", ["abc", "def"])
@pytest.mark.parametrize("y", [1, 2])
def test_parameters_stacking(x, y):
    pass


#
# Separate test IDs from test data
#
cases = {
    "base10": ("159", 10, 159),
    "base16": ("0xa", 16, 10),
}


@pytest.mark.parametrize("input_value,base,expected", cases.values(), ids=cases)
def test_with_ids(input_value, base, expected):
    assert int(input_value, base) == expected


#
# Embedded IDs
#
cases2 = [
    pytest.param("159", 10, 159, id="base 10"),
    pytest.param("0xa", 16, 10, id="base 16"),
]


@pytest.mark.parametrize("input_value, base, expected", cases2)
def test_with_embedded_ids(input_value, base, expected):
    assert int(input_value, base) == expected


#
# Test case from YAML
#
def load_test_cases(filename):
    with open(filename) as stream:
        contents = yaml.safe_load(stream)
        labels = contents["labels"]
        test_cases = [
            pytest.param(*data["values"], id=data["id"])
            for data in contents["test_cases"]
        ]
        return labels, test_cases


@pytest.mark.parametrize(*load_test_cases("test_data.yaml"))
def test_data_from_file(input_value, base, expected):
    assert int(input_value, base) == expected


#
# Another way to organize YAML test case
#
with open(pathlib.Path(__file__).with_name("test_data2.yaml")) as stream:
    contents = yaml.safe_load(stream)

TEST_CASES2 = [
    pytest.param(
        data["input_value"],
        data["base"],
        data["expected"],
        id=data["id"],
    )
    for data in contents
]


@pytest.mark.parametrize("input_value,base,expected", TEST_CASES2)
def test_data_from_file2(input_value, base, expected):
    assert int(input_value, base) == expected


#
# Yet another way, another yaml format
#
with open(pathlib.Path(__file__).with_name("test_data3.yaml")) as stream:
    data = yaml.safe_load(stream)
TEST_CASES3 = [pytest.param(*param, id=tid) for tid, param in data.items()]


@pytest.mark.parametrize("input_value,base,expected", TEST_CASES3)
def test_data_from_file3(input_value, base, expected):
    assert int(input_value, base) == expected
