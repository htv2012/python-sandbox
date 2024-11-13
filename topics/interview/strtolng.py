#!/usr/bin/python
import sys
import unittest

def string2long(buffer):
    digits = list(buffer)       # Convert the string to a list of digits
    if digits[0] == '-':
        sign = -1
        digits.remove('-')
    else:
        sign = 1
        
    number = 0
    for d in digits:
        number = number * 10 + int(d)
    number = number * sign;
    return number
    
class testString2Long(unittest.TestCase): 
    def test01(self):
        self.assertEqual(0, string2long("0"))
    def test02(self):
        self.assertEqual(-1, string2long("-1"))
    def test03(self):
        self.assertEqual(1, string2long("1"))
    def test04(self):
        self.assertEqual(-987654321, string2long("-987654321"))
    def test05(self):
        self.assertEqual(12345, string2long("12345"))
    def test06(self):
        self.assertEqual(32767, string2long("32767"))
    def test07(self):
        self.assertEqual(-32768, string2long("-32768"))
    def testMaxInt(self):
        self.assertEqual(sys.maxsize, string2long(str(sys.maxsize)))
    def testMinInt(self):
        self.assertEqual(-1 - sys.maxsize, string2long(str(-1 - sys.maxsize)))

if __name__ == '__main__':
    unittest.main()