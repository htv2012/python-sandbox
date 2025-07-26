from io import StringIO
import logging

logger = logging.getLogger('log_to_string')
logger.setLevel(logging.DEBUG)

buffer = StringIO()
handler = logging.StreamHandler(buffer)
handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger.addHandler(handler)

logger.info('This is information')
logger.debug('Debugging stuff')
logger.warning('Out of beer')

print('Buffer:')
print('---')
print(buffer.getvalue())
print('---')
