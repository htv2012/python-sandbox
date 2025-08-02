import pytest
from args_builder.handler import to_args


@pytest.mark.parametrize(
    ["indict", "expected"],
    [
        pytest.param({}, [], id="empty"),
        pytest.param(dict(verbose=""), ["--verbose"], id="is_flag"),
        pytest.param(
            dict(prologue="this is prologue"),
            ["--prologue", "this is prologue"],
            id="happy path",
        ),
        pytest.param(
            dict(insert_header=""), ["--insert-header"], id="underscore to dash"
        ),
        pytest.param(
            dict(define=["foo", "bar"]), ["--define", "foo", "bar"], id="multiple args"
        ),
    ],
)
def test_to_args(indict, expected):
    assert list(to_args(indict)) == expected
