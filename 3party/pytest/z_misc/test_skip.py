#!/usr/bin/env python3
import os
import platform

import pytest


@pytest.mark.skip(reason="Demo: skip a test")
def test_aways_failed():
    assert 0


@pytest.mark.skipif(platform.system() != "Windows", reason="Windows only")
def test_get_windir():
    windir = os.getenv("WINDIR")
    assert windir is not None
