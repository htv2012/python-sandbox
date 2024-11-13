#!/usr/bin/env python3
"""
Capture stdout and stderr by adding a `capfd` parameter to the test
function
"""

import os


def test_capture_stderr(capfd):
    os.system("ls /foo")
    captured = capfd.readouterr()
    assert "No such file" in captured.err


def test_capture_stdout(capfd):
    os.system("which env")
    captured = capfd.readouterr()
    assert captured.out == "/usr/bin/env\n"
