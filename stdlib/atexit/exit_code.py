#!/usr/bin/env python

import atexit
import os
import platform
import subprocess
import sys


@atexit.register
def bye():
    print('Goodbye')

def main():
    sys.argv.append('0')
    exit_code = int(sys.argv[1])
    print('Exiting with code', exit_code)
    exit(exit_code)

if __name__ == '__main__':
    try:
        main()
    except SystemExit as exc:
        if 'TUBE_NOTIFY' in os.environ:
            command = [os.path.abspath(os.environ['TUBE_NOTIFY']), str(exc.code)]
            print('Command:', command)
            subprocess.call(command, shell=('Windows' == platform.system()))
        raise