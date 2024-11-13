#!/usr/bin/env python
# encoding: utf-8
"""
compare_tests.py

Created by Hai Vu on 2010-07-22.
Copyright (c) 2010 Cisco Systems, Inc.. All rights reserved.
"""

import sys
import os
import unittest2 as unittest
from lxml import etree
from io import StringIO

# ======================================================================
#
# Function under test
#
# ======================================================================

class VerifyXml(object):
    reason = None

    def __init__(self, expected, actual, ignoreTags=[]):
        self.expected = self._get_root(expected)
        self.actual = self._get_root(actual)
        self.verified = self._verify_xml(self.expected, self.actual, ignoreTags)

    def _get_root(self, filename_or_string):
        '''
        Given a string representing a file name or an XML block, parse it
        and return the root of the XML document
        '''
        if type(filename_or_string) == str:
            if (os.path.exists(filename_or_string)):
                stream = open(filename_or_string)
            else:
                stream = StringIO(filename_or_string)
        else:
            raise TypeError('Invalid type: Expect a string or file name')

        doc = etree.parse(stream)
        stream.close()
        root = doc.getroot()
        return root

    def _verify_xml(self, expected, actual, ignoreTags=[]):
        # Compare the node's tag and text
        if actual.tag != expected.tag:
            self.reason = 'Expected: <%s>, actual: <%s>' % (expected.tag, actual.tag)
            return False

        if not (actual.text == expected.text or actual.tag in ignoreTags):
            exp = etree.tostring(expected).rstrip(' \n')
            act = etree.tostring(actual).rstrip(' \n')
            self.reason = 'Expected: %s, actual: %s' % (exp, act)
            return False

        # Compare the attributes
        expectedAttributes = set(expected.items())
        actualAttributes = set(actual.items())
        if expectedAttributes != actualAttributes:
            self.reason = 'Expected: %s, actual: %s' % (expectedAttributes, actualAttributes)
            return False

        # Compare the number of children
        expectedChildren = set(expected.getchildren())
        expectedChildrenCount = len(expectedChildren)
        actualChildren = set(actual.getchildren())
        actualChildrenCount = len(actualChildren)

        if expectedChildrenCount != actualChildrenCount:
            self.reason = 'Mismatched children count. Expected: %d, actual: %d' % (expectedChildrenCount, actualChildrenCount)
            return False

        # compare the chidren
        while len(expectedChildren) > 0:
            expectedNode = expectedChildren.pop()
            nodeMatched = False

            # We use xpath to filter out those child nodes from the
            # actual that do not have the same node tag as we won't
            # compare those against this expected node
            qualifiedChildren = actual.xpath(expectedNode.tag)
            for actualNode in qualifiedChildren:
                if self._verify_xml(expectedNode, actualNode, ignoreTags):
                    nodeMatched = True
                    break

            if not nodeMatched:
                return False

            actualChildren.remove(actualNode)

        return True

# ======================================================================
#
# Unit tests
#
# ======================================================================


class TestPrimitive(unittest.TestCase):
    def setUp(self):
        self.expected = '<message src="foo" code="501">hello</message>'

    def test_differentTagsExpectNotVerify(self):
        actual = '<msg>hello</msg>'
        v = VerifyXml(self.expected, actual)
        self.assertFalse(v.verified)
        self.assertEqual(
            'Expected: <message>, actual: <msg>',
            v.reason)

    def test_differentTextExpectNotVerify(self):
        actual = '<message>hi</message>'
        v = VerifyXml(self.expected, actual)
        self.assertFalse(v.verified)
        self.assertEqual(
            'Expected: <message src="foo" code="501">hello</message>, actual: <message>hi</message>',
            v.reason)

    def test_sameAttributesExpectVerify(self):
        actual = '<message code="501" src="foo">hello</message>'
        v = VerifyXml(self.expected, actual)
        self.assertTrue(v.verified)

    def test_differentNumberOfAttributesExpectNotVerify(self):
        actual = '<message id="1" code="501" src="foo">hello</message>'
        v = VerifyXml(self.expected, actual)
        self.assertFalse(v.verified)
        self.assertEqual(
            "Expected: set([('code', '501'), ('src', 'foo')]), actual: set([('code', '501'), ('src', 'foo'), ('id', '1')])",
            v.reason)


class TestComplex(unittest.TestCase):
    def setUp(self):
        self.expected = 'data/expected.xml'

    def test_indenticalExpectVerified(self):
      actual = 'data/expected.xml'
      v = VerifyXml(self.expected, actual)
      self.assertTrue(v.verified)

    def test_ignoreTagsExpectVerified(self):
        actual = 'data/ignore_tags.xml'
        ignoreTags = ['ObjectId', 'SmtpAddress']
        v = VerifyXml(self.expected, actual, ignoreTags)
        self.assertTrue(v.verified)

    def test_ignoreTagsExpectNotVerify(self):
        actual = 'data/ignore_tags.xml'
        ignoreTags = ['ObjectId']
        v = VerifyXml(self.expected, actual, ignoreTags)
        self.assertFalse(v.verified)
        self.assertEqual(
            'Expected: <SmtpAddress>dirsearch_user_0501@qa-ks-vm-7.cisco.com</SmtpAddress>, actual: <SmtpAddress>dontcare3</SmtpAddress>',
            v.reason)

    def test_childrenOutOfOrderExpectVerified(self):
        actual = 'data/out_of_order.xml'
        v = VerifyXml(self.expected, actual)
        self.assertTrue(v.verified)

    def test_childrenCountNotMatchedExpectNotVerified(self):
        actual = 'data/child_count_mismatched.xml'
        v = VerifyXml(self.expected, actual)
        self.assertFalse(v.verified)
        self.assertEqual(
            'Mismatched children count. Expected: 3, actual: 2',
            v.reason)

    def test_actualChildDifferentExpectNotVerified(self):
        actual = 'data/child_mismatched.xml'
        v = VerifyXml(self.expected, actual)
        self.assertFalse(v.verified)
        self.assertEqual(
            'Expected: <DtmfAccessId>1503</DtmfAccessId>, actual: <DtmfAccessId>150</DtmfAccessId>',
            v.reason)

if __name__ == '__main__':
	unittest.main()