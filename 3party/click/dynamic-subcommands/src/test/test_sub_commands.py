import pytest

from dynamic_subcommands import main


def test_subcommand(runner, subcommand):
    res = runner.invoke(main, [subcommand])
    assert res.exit_code == 0


@pytest.mark.parametrize(
    argnames=["subcmd"],
    argvalues=[
        ("foo",),
        ("pu",),
        ("ge",),
    ],
)
def test_invalid_subcommand(runner, subcmd):
    res = runner.invoke(main, [subcmd])
    assert res.exit_code == 2
