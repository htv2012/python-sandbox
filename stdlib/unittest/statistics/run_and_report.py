import unittest
from collections import namedtuple

TestStat = namedtuple('TestStat', ['name', 'message'])


def parse_test_stat(stat):
	"""
	Parse a stat
	:param stat: A tuple of (test_object, message)
	:return: A TestStat object
	"""
	test_stat = TestStat(stat[0].id(), stat[1])
	return test_stat

def print_list(stats, verbose=False):
	test_stats = map(parse_test_stat, stats)
	longest_column = max(len(t.name) for t in test_stats)
	for name, message in test_stats:
		if verbose:
			print '{name:<{w}}: {message}'.format(name=name, message=message, w=longest_column)
		else:
			print name

module_name = 'test_something'
loader = unittest.TestLoader()
suite = loader.loadTestsFromName(module_name)
result = unittest.TestResult()
suite.run(result)

# Statistics
print 'Module:', module_name
print 'Total:', result.testsRun
print 'Failures:', len(result.failures)
print 'Errors:', len(result.errors)
print 'Skipped:', len(result.skipped)
print ''

print 'Failed Tests:'
print_list(result.failures)
print ''

print 'Skipped Tests:'
print_list(result.skipped, verbose=True)
print ''

