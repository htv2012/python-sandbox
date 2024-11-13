#!/usr/bin/env python


import sys
from smb.SMBConnection import SMBConnection


def main():
    connection = SMBConnection('haiv', '', 'haimac.local', 'dakao.local')
    if not connection.connect('10.0.0.4'):
        print('Failed to connect')
        return 1

    with open(__file__) as f:
        connection.storeFile('temp', '/foo/smb_tryout2.py', f)

    files_list = connection.listPath('temp', '/')
    for f in files_list:
        print(f.filename)

if __name__ == '__main__':
    sys.exit(main())

