import pytest


def test_expect_raise():
    dict_object = {}
    with pytest.raises(KeyError):
        dict_object["foo"]
