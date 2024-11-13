from sut import double


def test_zero():
    assert 0 == double(0)

def test_negative_int():
    assert -10 == double(-5)

def test_positive_int():
    assert 50 == double(25)

def test_positive_float():
    assert 100.0 == double(50.0)

def test_string():
    assert 'abcabc' == double('abc')
