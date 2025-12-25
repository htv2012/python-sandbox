import pytest

from frozen_dict import frozendict

# dut: dictionary under test


def test_empty_dict():
    dut = frozendict()
    assert len(dut) == 0
    assert list(dut) == []
    hash(dut)


dicts = [
    pytest.param(frozendict(a=1, b=2, c=3), id="from iterable"),
    pytest.param(frozendict({"a": 1, "b": 2, "c": 3}), id="from dict"),
    pytest.param(
        frozendict(frozendict({"a": 1, "b": 2, "c": 3})), id="from frozendict"
    ),
]


@pytest.mark.parametrize("dut", dicts)
def test_dict_characteristics(dut):
    assert len(dut) == 3
    assert dut["a"] == 1
    assert dut["b"] == 2
    assert dut["c"] == 3
    assert list(dut) == ["a", "b", "c"]
    assert list(dut.items()) == [("a", 1), ("b", 2), ("c", 3)]


@pytest.mark.parametrize("dut", dicts)
def test_hashable(dut):
    hash(dut)


@pytest.mark.parametrize("dut", dicts)
def test_add_key(dut):
    with pytest.raises(TypeError):
        dut["d"] = 4


@pytest.mark.parametrize("dut", dicts)
def test_modify(dut):
    with pytest.raises(TypeError):
        dut["c"] = 30


@pytest.mark.parametrize("dut", dicts)
def test_hack_failed(dut):
    with pytest.raises(AttributeError):
        dut.__data["c"] = 30
