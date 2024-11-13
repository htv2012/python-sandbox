import pytest
from sut import double

test_data = [
    (0, 0),
    (5, 10),
    (-71, -142),
    (5.5, 11.0),
    (-7.1, -14.2),
    ('xyz', 'xyzxyz'),
]

@pytest.mark.parametrize('x, two_x', test_data)
def test_double(x, two_x):
    assert two_x == double(x)
