"""
How to request a temp dir: by adding a parameter named `tmp_path`
"""

import logging
import pathlib


def test_that_need_a_temp_dir(tmp_path):
    filename = pathlib.Path(tmp_path) / "data.txt"
    logging.debug("filename=%r", filename)

    assert not filename.exists()
