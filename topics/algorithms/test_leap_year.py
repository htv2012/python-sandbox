from leap_year import is_leap_year


def test_400():
    assert is_leap_year(2000)
    assert is_leap_year(1600)
    assert is_leap_year(1200)


def test_100():
    assert is_leap_year(1900) is False
    assert is_leap_year(1800) is False
    assert is_leap_year(1700) is False


def test_4():
    assert is_leap_year(2004)
    assert is_leap_year(1984)


def test_non_leap():
    assert is_leap_year(1959) is False
    assert is_leap_year(2002) is False
