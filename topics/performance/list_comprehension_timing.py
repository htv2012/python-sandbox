#!/usr/bin/env python

import timeit

setup = '''
masterList = range(1000)
subList = [4,5,6,7,1,11,21,31,41,51,61,71,81,91, 2000, 3000, 4000]
'''

statement1 = 'result = [i for i in masterList if i in subList]'
t1 = timeit.Timer(statement1, setup=setup)
print('Comprehensive: %7.3f' % t1.timeit(number=1000))

statement2 = '''
for i in masterList[:]:
    if i not in subList:
        masterList.remove(i)
'''
t2 = timeit.Timer(statement2, setup=setup)
print('Loop:          %7.3f' % t2.timeit(number=1000))

