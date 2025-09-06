import pathlib

import pytest

from roman_numerals import arabic, roman


def load_test_data(filename: str):
    path = pathlib.Path(__file__).with_name(filename)

    def convert(text: str):
        try:
            return int(text)
        except ValueError:
            return text

    with open(path) as stream:
        for line in stream:
            yield [convert(x) for x in line.split()]


@pytest.mark.parametrize(["ara", "expected"], load_test_data("arabic2roman.txt"))
def test_arabic_to_roman(ara, expected):
    assert roman(ara) == expected


@pytest.mark.parametrize(["expected", "rom"], load_test_data("arabic2roman.txt"))
def test_roman_to_arabic(expected, rom):
    assert arabic(rom) == expected
