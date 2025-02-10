import pathlib

import pytest
from click.testing import CliRunner


#
# Support functions
#
def _get_subcommands():
    """Get a list of subcommands from the commands/cmd_*.py files"""
    test_dir = pathlib.Path(__file__).parent
    commands_dir = test_dir.parent / "dynamic_subcommands" / "commands"
    commands_list = sorted(
        path.stem.removeprefix("cmd_") for path in commands_dir.glob("cmd_*.py")
    )
    return commands_list


#
# Fixtures
#


@pytest.fixture(scope="session")
def runner():
    return CliRunner()


@pytest.fixture(params=_get_subcommands())
def subcommand(request):
    """Return a list of commands, e.g. ['get', 'put']"""
    return request.param
