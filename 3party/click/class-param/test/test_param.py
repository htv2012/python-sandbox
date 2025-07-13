import dataclasses
from unittest.mock import Mock

import click
import pytest

from class_param.clicklib import ClassParamType


@dataclasses.dataclass
class MyClass:
    ivar: int
    fvar: float
    bvar: bool
    svar: str

    param_type = dict(ivar=int, fvar=float, bvar=bool, svar=str)


@pytest.fixture
def param_type():
    return ClassParamType(MyClass)


@pytest.fixture
def mock_param():
    return Mock()


@pytest.fixture
def mock_ctx():
    return Mock()


@pytest.mark.parametrize(
    ["value", "expected_svar"],
    [
        pytest.param("3,3.5,true,hello", "hello", id="args only"),
        pytest.param("3,3.5,true,hello world", "hello world", id="args contain spaces"),
        pytest.param("3,3.5,true,svar=hello", "hello", id="args and kwargs"),
        pytest.param("ivar=3,fvar=3.5,svar=hello,bvar=true", "hello", id="kwargs"),
        pytest.param(
            "ivar=3,fvar=3.5,svar=hello world,bvar=true",
            "hello world",
            id="kwargs with spaces",
        ),
    ],
)
def test_convert_expect_pass(value, expected_svar, param_type, mock_param, mock_ctx):
    actual = param_type.convert(value, mock_param, mock_ctx)
    assert actual.ivar == 3
    assert actual.fvar == 3.5
    assert actual.bvar is True
    assert actual.svar == expected_svar


@pytest.mark.parametrize(
    ["value"],
    [
        pytest.param("foo,3.5,true,hello", id="incorrect type for arg"),
        pytest.param("bvar=5", id="incorrect type for kwarg"),
    ],
)
def test_convert_expect_fail(value, param_type, mock_param, mock_ctx):
    with pytest.raises(click.BadParameter):
        param_type.convert(value, mock_param, mock_ctx)
