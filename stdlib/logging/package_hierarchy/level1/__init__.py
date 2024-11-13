import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(levelname)s|%(name)s: %(message)s'
# )
formatter = logging.Formatter('%(levelname)s|%(name)s: %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)

logger.info('Initialize level1')
