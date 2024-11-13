#!/usr/bin/env python
# encoding: utf-8
"""
sample2.py

Created by Hai Vu on 2013-05-29.
Copyright (c) 2013 High View Software. All rights reserved.
"""

import argparse
import argparse_actions2 as argparse_actions

def ip_tryout(args):
    parser = argparse.ArgumentParser(description='Custom Actions')
    parser.add_argument('ip', action=argparse_actions.ValidIpAction, nargs=len(args))
    
    try:
        args = parser.parse_args(args)
        print('IP: {0}'.format(args.ip))
    except argparse_actions.InvalidIp as e:
        print('Bad IP: {0}'.format(e.ip))
        # print e # ==> This works, too.
        
def main():
    ip_tryout(['10.0.0.93'])
    ip_tryout(['10.0.0.256'])
    ip_tryout(['10.0.999'])
    ip_tryout(['10.0.9.5.3'])
    ip_tryout(['10.0.0.25', '10.93.255.36'])
    ip_tryout(['10.0.0.25', '256.0.0.1', '10.93.255.36'])
    
if __name__ == '__main__':
	main()

