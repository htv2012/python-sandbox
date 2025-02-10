import pytest

from dynamic_subcommands import main


@pytest.fixture()
def result(runner):
    """Result of invoking without any sub command"""
    res = runner.invoke(main)
    return res


def test_exit_code(result):
    """Verify the exit code to the shell"""
    assert result.exit_code == 0


def test_return_value(result):
    """Verify the return value of function main"""
    assert result.return_value is None


def test_exception(result):
    """Verify no exception occured"""
    assert result.exception is None


def test_subcommands_found_in_help(result, subcommand):
    """Verify the commands are present in help message"""
    lines = [line.strip() for line in result.stdout.splitlines()]
    assert any(line.startswith(subcommand) for line in lines)
