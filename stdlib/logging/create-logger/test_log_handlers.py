import os

import pytest

from log_handlers import get_logger_filename


@pytest.mark.parametrize(
    ["file_exists"],
    [
        pytest.param(True, id="log file exists"),
        pytest.param(False, id="log file does not exist"),
    ],
)
def test_get_logger_filename_with_none_str(tmp_path, file_exists):
    os.chdir(tmp_path)
    if file_exists:
        (tmp_path / "none").touch(exist_ok=True)

    assert get_logger_filename("none", False, "mode") == "none"


def test_get_logger_filename_with_non_existent_custom_name(tmp_path):

