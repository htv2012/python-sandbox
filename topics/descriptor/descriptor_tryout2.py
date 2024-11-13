
import logging
from weakref import WeakKeyDictionary


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Cardinal(object):
	def __init__(self, value):
		logger.debug('Cardinal.init: value={}'.format(value))
		self.default = value
		self.data = WeakKeyDictionary()

	def __get__(self, obj, objtype):
		logger.debug('Cardinal.get: self={!r}, obj={!r}, objtype={}'.format(self, obj, objtype))
		return self.data.get(obj, self.default)

	def __set__(self, obj, value):
		logger.debug('Cardinal.set: self={!r}, obj={!r}, value={!r}'.format(self, obj, value))
		logger.debug('Before set, data={!r}'.format(self.data))

		if not isinstance(value, (int, float)):
			raise TypeError('Value must be int or float: {!r}'.format(value))

		if value < 0:
			raise ValueError('Negative not allowed: {}'.format(value))

		self.data[obj] = value
		logger.debug('After set, data={!r}'.format(self.data))


class Movie(object):
	budget = Cardinal(0)
	gross = Cardinal(0)

	def __init__(self, title, budget, gross):
		logger.debug('Movie.init: title={title!r}, budget={budget!r}, gross={gross!r}'.format(**locals()))

		self.title = title
		self.budget = budget
		self.gross = gross


class Documentary(Movie):
	def __init__(self, title, budget, gross, topic):
		logger.debug('Documentary.init: topic={!r}'.format(topic))

		super(Documentary, self).__init__(title, budget, gross)
		self.topic = topic


if __name__ == '__main__':
	m1 = Movie('Point X', 10, 15)
	print('Budget:', m1.budget)
	m1.budget = 12
	print('Budget after set to 12:', m1.budget)

	try:
		m1.budget = -3
	except Exception as e:
		print(e)
	print('Budget:', m1.budget)

	try:
		m1.budget = 'too much'
	except Exception as e:
		print(e)
	print('Budget:', m1.budget)

	print('------------------------------------------------------------')

	m2 = Movie('Happy Cow', 8, 19)
	print('M1 budget:', m1.budget)
	print('M2 budget:', m2.budget)

	print('------------------------------------------------------------')
	print('Documentary 1')
	print('------------------------------------------------------------')
	d1 = Documentary('Bleu', 5, 11, 'Nature')
