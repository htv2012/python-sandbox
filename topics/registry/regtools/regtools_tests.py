"""
Test functionality of regtools
"""

import contextlib
import unittest
import winreg

STRING_NAME = "StringValue"
STRING_VALUE = "abc"

ROOT = winreg.HKEY_CURRENT_USER
REGTOOLS_DIR = "Software\\regtools"
RESERVED = 0


@contextlib.contextmanager
def folder_context(root, path, permission=winreg.KEY_READ):
    folder = winreg.OpenKey(path, REGTOOLS_DIR, RESERVED, permission)
    yield folder
    winreg.CloseKey(folder)


class RegToolsTests(unittest.TestCase):
    def setUp(self):
        winreg.CreateKey(ROOT, REGTOOLS_DIR)
        with folder_context(ROOT, REGTOOLS_DIR, winreg.KEY_WRITE) as folder:
            winreg.SetValueEx(
                folder, STRING_NAME, RESERVED, winreg.REG_SZ, STRING_VALUE
            )


if __name__ == "__main__":
    unittest.main()
