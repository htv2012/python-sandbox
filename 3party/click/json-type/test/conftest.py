import pytest

from json_type.clicklib import EnumParamType, JsonParamType

from .sample import SampleEnum, User


@pytest.fixture
def convert_enum():
    param_type = EnumParamType(SampleEnum)
    return param_type.convert


@pytest.fixture
def convert_user():
    param_type = JsonParamType(User)
    return param_type.convert


@pytest.fixture
def convert_json():
    param_type = JsonParamType()
    return param_type.convert


@pytest.fixture(scope="session")
def data_path(pytestconfig):
    return pytestconfig.rootpath / "test" / "data"
