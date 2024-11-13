#!/usr/bin/env python

import subprocess

cmd = 'svn status --non-interactive --no-ignore'.split()
pipe = subprocess.Popen(
        cmd,
        cwd='/Users/haiv/cpve/trunk',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
stdout, stderr = pipe.communicate()

print('stderr = \n{}'.format(stderr))
print('stdout = \n{}'.format(stdout))