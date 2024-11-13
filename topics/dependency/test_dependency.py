import pytest

from dependency import Dependency


@pytest.fixture(scope="class")
def simple():
    dependency = Dependency()
    dependency.add("A", "BCD")
    return dependency


@pytest.fixture(scope="class")
def complex():
    dependency = Dependency()
    dependency.add("A", "BC")
    dependency.add("B", "CD")
    dependency.add("C", "EF")
    return dependency


class TestSimple:
    def test_nodes(self, simple):
        assert list(simple.nodes()) == list("ABCD")

    def test_resolve(self, simple):
        assert list(simple.resolve()) == [set("BCD"), set("A")]

    def test_serial_resolve(self, simple):
        actual = list(simple.serial_resolve())
        assert set(actual[:3]) == set("BCD")
        assert actual[-1] == "A"


class TestComplex:
    def test_nodes(self, complex):
        assert set(complex.nodes()) == set("ABCDEF")

    def test_resolve(self, complex):
        assert list(complex.resolve()) == [
            set("DEF"),
            set("C"),
            set("B"),
            set("A"),
        ]

    def test_serial_resolve(self, complex):
        actual = list(complex.serial_resolve())
        assert set(actual[:3]) == set("DEF")
        assert actual[3:] == list("CBA")
