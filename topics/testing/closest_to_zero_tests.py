
import pytest


def closest(li):
    li2 = ((x, abs(x)) for x in li)
    result, last_abs = next(li2)
    for number, current_abs in li2:
        if current_abs < last_abs:
            result = number

    return result


test_data = [
    ((1, 2, 3), 1),
    ((-5, 7, 4, 2), 5),
]


def test_closest():
    for the_list, expected in test_data:
        actual = closest(the_list)
        assert actual == expected, "For input {}, expected {}, got {}".format(
            the_list, expected, actual
        )


if __name__ == "__main__":
    pytest.main([__file__])
