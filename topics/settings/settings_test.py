#!/usr/bin/env python
# encoding: utf-8
"""
settings_test.py

Created by Hai Vu on 2014-03-25
Copyright (c) 2014 Hai Vu. All rights reserved.
"""

import os
import unittest

import settings

settings_string = """
string_info = 'machine1.local'
int_info = 1936
float_info = 3.59
list_info = [1,2,3]
dict_info = {'John':1, 'Anna':2}
"""


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self._base_filename = "settings_test"
        self.settings_file = os.path.expanduser("~/." + self._base_filename)
        with open(self.settings_file, "w") as f:
            f.write(settings_string)
        self.config = settings.load(self._base_filename)
        self.s = settings.Settings(self._base_filename)

    @classmethod
    def tearDownClass(self):
        os.remove(self.settings_file)


class SettingsTest(BaseTest):
    def verify_setting(self, setting_name, expected_value):
        actual_value = self.config.get(setting_name)
        self.assertEqual(expected_value, actual_value)

    def test_keys_count(self):
        self.assertEqual(5, len(self.config))

    def test_string(self):
        self.verify_setting("string_info", "machine1.local")

    def test_int(self):
        self.verify_setting("int_info", 1936)

    def test_float(self):
        self.verify_setting("float_info", 3.59)

    def test_list(self):
        self.verify_setting("list_info", [1, 2, 3])

    def test_dict(self):
        self.verify_setting("dict_info", {"Anna": 2, "John": 1})

    def test_file_not_found(self):
        config = settings.load("scobydobydo")
        self.assertEqual({}, config)


class SettingsObjectTest(BaseTest):
    def test_keys_count(self):
        self.assertEqual(5, len(self.s))

    def test_string(self):
        self.assertEqual("machine1.local", self.s.string_info)

    def test_int(self):
        self.assertEqual(1936, self.s.int_info)

    def test_float(self):
        self.assertEqual(3.59, self.s.float_info)

    def test_list(self):
        self.assertEqual([1, 2, 3], self.s.list_info)

    def test_dict(self):
        self.assertEqual({"Anna": 2, "John": 1}, self.s.dict_info)

    def test_file_not_found(self):
        s = settings.Settings("scobydobydo")
        self.assertEqual(0, len(s))


if __name__ == "__main__":
    unittest.main()
