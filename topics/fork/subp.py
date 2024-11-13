#!/usr/bin/env python

import os, sys, time
import subprocess

def main():
    print(('subp.py\t pid=%d' % os.getpid()))
    p = subprocess.Popen(['/usr/bin/env', 'python', 'child.py'])
    print(('subp.py\tp=%s' % p))
    time.sleep(10)
    p.terminate()

if __name__ == '__main__':
    main()
