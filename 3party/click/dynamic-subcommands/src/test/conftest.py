import pathlib

import pytest
from click.testing import CliRunner


@pytest.fixture(scope="session")
def runner():
    return CliRunner()


def get_subcommands():
    """Get a list of subcommands from the commands/cmd_*.py files"""
    test_dir = pathlib.Path(__file__).parent
    commands_dir = test_dir.parent / "dynamic_subcommands" / "commands"
    commands_list = sorted(
        path.stem.removeprefix("cmd_") for path in commands_dir.glob("cmd_*.py")
    )
    return commands_list


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "subcommand" in metafunc.fixturenames:
        metafunc.parametrize("subcommand", get_subcommands())
