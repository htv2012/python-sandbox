#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
import os
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    print 'cElementTree is not available, try ElementTree'
    import xml.etree.ElementTree as ET


H_ERROR_CLASS = 'Error Class'
H_ERROR_REASON = 'Error Reason'
H_FAILURE_CLASS = 'Failure Class'
H_FAILURE_REASON = 'Failure Reason'
H_SKIP_CLASS = 'Skipped Class'
H_SKIP_REASON = 'Skipped Reason'
H_TEST_CLASS = 'Test Class'
H_TEST_DURATION = 'Test Duration'
H_TEST_NAME = 'Tet Name'


def get_exception(exception_hierarchy):
    return exception_hierarchy.split('.')[-1]


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('xunit', type=argparse.FileType(mode='r'))
    parser.add_argument('csv', type=argparse.FileType(mode='wb'))
    options = parser.parse_args()
    return options

if __name__ == '__main__':
    # Hack for faster developement, remove after done
    sys.argv.append('/Users/haiv/Dropbox/src/python/unittest/results.xml')
    sys.argv.append('/Users/haiv/Dropbox/src/python/unittest/results.csv')

    options = get_options()

    header = [
        H_TEST_CLASS, H_TEST_NAME, H_TEST_DURATION,
        H_FAILURE_CLASS, H_FAILURE_REASON,
        H_SKIP_CLASS, H_SKIP_REASON,
        H_ERROR_CLASS, H_ERROR_REASON]
    writer = csv.DictWriter(options.csv, header)
    writer.writeheader()

    tree = ET.parse(options.xunit)
    suite = tree.getroot()

    # Summary
    print 'Summary:',
    print ', '.join('{}={}'.format(*kv) for kv in suite.items())

    for tc in suite.findall('testcase'):
        row = {
            H_TEST_CLASS: tc.get('classname'),
            H_TEST_NAME: tc.get('name'),
            H_TEST_DURATION: tc.get('time'),
        }

        for node in tc.getchildren():
            if node.tag == 'failure':
                row[H_FAILURE_CLASS] = get_exception(node.get('type'))
                row[H_FAILURE_REASON] = node.get('message')
            elif node.tag == 'skipped':
                row[H_SKIP_CLASS] = get_exception(node.get('type'))
                row[H_SKIP_REASON] = node.get('message')
            elif node.tag == 'error':
                row[H_ERROR_CLASS] = get_exception(node.get('type'))
                row[H_ERROR_REASON] = node.get('message')

        writer.writerow(row)