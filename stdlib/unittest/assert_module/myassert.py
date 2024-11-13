""" Provide all the assert* goodness outside of unittest.TestCase """
import unittest
import sys
sys.modules[__name__] = unittest.TestCase('longMessage')
