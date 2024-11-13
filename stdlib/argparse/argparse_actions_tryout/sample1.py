#!/usr/bin/env python
# encoding: utf-8
"""
sample1.py

Created by Hai Vu on 2013-05-29.
Copyright (c) 2013 High View Software. All rights reserved.
"""

import argparse
import argparse_actions

def main():
    parser = argparse.ArgumentParser(description='Custom Actions')
    parser.add_argument('directory', action=argparse_actions.VerifyFolderAction)
    
    try:
        args = parser.parse_args()
        print('Directory is: {0}'.format(args.directory))
    except argparse_actions.NonFolderError as e:
        print(args, e)

if __name__ == '__main__':
	main()

