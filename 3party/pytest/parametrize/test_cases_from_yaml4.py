import pathlib

import pytest
import yaml

# Load test cases
with open(pathlib.Path(__file__).with_name("test_data4.yaml")) as stream:
    TEST_CASES = [
        pytest.param(*data["args"], **data["kwargs"]) for data in yaml.safe_load(stream)
    ]


@pytest.mark.parametrize("input_value,base,expected", TEST_CASES)
def test_str2int(input_value, base, expected):
    assert int(input_value, base) == expected
