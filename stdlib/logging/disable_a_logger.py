#!/usr/bin/env python3
import contextlib
import logging


@contextlib.contextmanager
def disable_logging(logger):
	saved_state = logger.disabled
	logger.disabled = True
	yield logger
	logger.disabled = saved_state


if __name__ == '__main__':
	# Uncomment this to see the effect of propagate
	# logging.basicConfig()
	
	logger = logging.getLogger(__name__)
	handler = logging.StreamHandler()
	logger.addHandler(handler)
	logger.setLevel(logging.DEBUG)

	logger.info("Before disabling")
	
	# Disable it using the unofficial way: the disabled attribute
	logger.disabled = True
	logger.info("You should not see this")

	# Re-enable
	logger.disabled = False
	logger.info("After re-enabling")

	# Disable using official documented way
	logger.propagate = False  # Do not propagate to parent logger
	logger.setLevel(logging.NOTSET)
	logger.info("You should not see this, part 2")

	# Re-enable
	logger.propagate = True  # Do not propagate to parent logger
	logger.setLevel(logging.DEBUG)
	logger.info("After re-enabling, part 2")

	# Disable by removing all handlers, not recommended, because we
	# will need to add them back
	logger.handlers = []
	logger.propagate = False
	logger.info("You should not see this, part 3")

	# Re-enable
	logger.addHandler(handler)
	logger.propagate = True
	logger.info("After re-enabling, part 3")

	# If needed several times, create a context managger for temporarily
	# disabling a logger
	with disable_logging(logger):
		logger.info("You should not see this, part 4")
	logger.info("After re-enabling, part 4")
