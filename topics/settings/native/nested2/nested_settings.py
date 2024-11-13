#!/usr/bin/env python
# encoding: utf-8
'''
nested_settings.py

Created by Hai Vu on 2011-10-09.
Copyright (c) 2011 Cisco Systems, Inc.. All rights reserved.
'''

import sys
import os
import settings

def main():
    print('Server')
    print('  Host: %s' % settings.server)
    print('  Port: %d' % settings.port)

    print('Users')
    print('  Admin user: %s' % settings.users.admin_user)
    print('  Admin password: %s' % settings.users.admin_password)


if __name__ == '__main__':
    main()

