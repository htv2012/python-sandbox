import pytest

from handler import CommandRequest, build_command


@pytest.mark.parametrize(
    ["command", "req", "expected"],
    [
        pytest.param(
            "mycmd",
            CommandRequest(
                global_kwargs=dict(verbose="", config_file="/tmp/config.txt"),
                command_id="make-fun",
                command_kwargs=dict(header="this is header"),
            ),
            [
                "mycmd",
                "--verbose",
                "--config-file",
                "/tmp/config.txt",
                "make-fun",
                "--header",
                "this is header",
            ],
            id="happy path",
        ),
        pytest.param(
            "mycmd",
            CommandRequest(global_kwargs={}, command_id="make-fun", command_kwargs={}),
            ["mycmd", "make-fun"],
            id="no option",
        ),
    ],
)
def test_build_command(command, req, expected):
    assert build_command(command, req) == expected
