import logging
import pathlib


def test_tmp_path(tmp_path: pathlib.Path):
    tmp_file = tmp_path / "data.txt"
    logging.debug("tmp_file=%r", tmp_file)
