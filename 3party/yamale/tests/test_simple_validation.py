#!/usr/bin/env python3
"""
Demonstrate how yamale validation works
"""
import pytest
import yamale


@pytest.fixture
def schema():
    data_schema = yamale.make_schema(content="age: int(max=100)\nname: str()")
    return data_schema


def test_data(schema):
    data = yamale.make_data(content="name: John\nage: 59\n")
    yamale.validate(schema, data)


def test_bad_name(schema):
    data = yamale.make_data(content="name: 9\nage: 59\n")
    yamale.validate(schema, data)

def test_age_too_big(schema):
    data = yamale.make_data(content="name: John\nage: 259\n")
    yamale.validate(schema, data)

def test_bad_age(schema):
    data = yamale.make_data(content="name: John\nage: old\n")
    yamale.validate(schema, data)

