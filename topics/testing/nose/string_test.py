#!/usr/bin/env python
# encoding: utf-8
"""
string_test.py

Created by Hai Vu on 2010-07-17.
Copyright (c) 2010 Cisco Systems, Inc.. All rights reserved.
"""

import unittest


def setUpModule():
    print("setUpModule")
    global xvar
    xvar = 5


def tearDownModule():
    print("tearDownModule")


class TestString(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def split_test(self):
        print("split_test")

    def xvar_test(self):
        global xvar
        print("xvar =", xvar)

    def join_test(self):
        print("join_test")
