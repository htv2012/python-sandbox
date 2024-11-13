#!/usr/bin/env python

class MyError(Exception):
    def __init__(self, msg, other_info):
        Exception.__init__(self, msg)
        self.other_info = other_info
    def __str__(self):
        return '{}'.format(self.other_info)

if __name__ == '__main__':
    try:
        raise MyError('my message', 'other info')
    except MyError as e:
        print('\n'.join(dir(e)))
        print('')
        print(e)
        
	