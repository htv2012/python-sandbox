from dynamic_subcommands import main


def test_subcommand(runner, subcommand):
    res = runner.invoke(main, [subcommand])
    assert res.exit_code == 0
