#!/usr/bin/env python
class Stack(object):
	class PopEmptyStack(Exception):
		pass

	#
	# The essentials
	#
	def __init__(self, iterable=None):
		self._data = list(iterable or [])

	def push(self, element):
		self._data.append(element)

	def pop(self):
		try:
			return self._data.pop()
		except IndexError:
			raise self.PopEmptyStack()

	def isempty(self):
		return not bool(self._data)

	#
	# Optional, convenient
	#
	def __repr__(self):
		return '{}({})'.format(self.__class__.__name__, self._data)

def main():
    """ Entry """
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print('Stack:', s)

    print('\nPopping:')
    while not s.isempty():
            e = s.pop()
            print(e)

    print('\nPop an empty stack:')
    try:
            s.pop()
    except Stack.PopEmptyStack as e:
            print('Got an exeption of type', type(e).__name__)


if __name__ == '__main__':
    main()
