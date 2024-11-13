import logging

def summarize():
	global console_formatter, console_handler

	console_handler.setFormatter(logging.Formatter('%(message)s'))
	logger.info('Here is my report')
	console_handler.setFormatter(console_formatter)

def interact():
	# Remove the console handler
	for handler in  logger.handlers:
		if not isinstance(handler, logging.FileHandler):
			saved_handler = handler
			logger.removeHandler(handler)
			break

	# Interact
	logger.info('to file only')

	# Add the console handler back
	logger.addHandler(saved_handler)

numlevel = logging.DEBUG
logfile = 'switch_format.log'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler(filename=logfile, mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s:%(funcName)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.info('Before summary')
summarize()
interact()
logger.info('After summary')

# 'Cat' the log file
print('\nFILE:')
print((open(logfile).read()))