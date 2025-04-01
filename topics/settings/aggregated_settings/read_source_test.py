#!/usr/bin/env python3
import io
import json

import pytest
import yaml

from settings import _read_source


def test_read_dict():
    input_object = dict(a=1, b=2)
    actual = _read_source(input_object)
    assert input_object == actual


def test_read_expect_error():
    with pytest.raises(ValueError):
        _read_source(1)


def test_read_json(tmpdir):
    expected = dict(a=1, b=2)
    json_file = tmpdir / "my.json"
    with open(json_file, "w") as stream:
        json.dump(expected, stream)

    json_filename = str(json_file)
    actual = _read_source(json_filename)

    assert actual == expected


def test_read_yaml(tmpdir):
    expected = dict(a=1, b=2)
    yaml_file = tmpdir / "my.yaml"
    with open(yaml_file, "w") as stream:
        yaml.dump(expected, stream)

    yaml_filename = str(yaml_file)
    actual = _read_source(yaml_filename)

    assert actual == expected


def test_read_json_file_object():
    expected = dict(a=1, b=2)
    with io.StringIO(json.dumps(expected)) as buffer:
        actual = _read_source(buffer)
        assert actual == expected


def test_read_yaml_file_object():
    expected = dict(a=1, b=2)
    with io.StringIO(yaml.dump(expected)) as buffer:
        actual = _read_source(buffer)
        assert actual == expected
