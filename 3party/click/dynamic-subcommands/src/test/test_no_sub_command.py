import pytest
from click.testing import CliRunner

from dynamic_subcommands import main


@pytest.fixture(scope="module")
def result():
    """Result of invoking without any sub command"""
    runner = CliRunner()
    res = runner.invoke(main)
    return res


@pytest.fixture
def commands(request):
    """A list of commands, figured dynamically"""
    test_dir = request.path.parent
    commands_dir = test_dir.parent / "dynamic_subcommands" / "commands"
    cmd_list = [
        path.stem.removeprefix("cmd_") for path in commands_dir.glob("cmd_*.py")
    ]
    return cmd_list


def test_exit_code(result):
    """Verify the exit code to the shell"""
    assert result.exit_code == 0


def test_return_value(result):
    """Verify the return value of function main"""
    assert result.return_value is None


def test_exception(result):
    """Verify no exception occured"""
    assert result.exception is None


def test_sub_commands_in_help(result, commands):
    """Verify the commands are present in help message"""
    lines = [line.strip() for line in result.stdout.splitlines()]
    for command in commands:
        assert any(line.startswith(command) for line in lines)
