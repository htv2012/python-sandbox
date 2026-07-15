import logging

# Get root logger (or use a module logger with __name__)
logger = logging.getLogger()  # or logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Remove existing handlers (prevents console logging)
for h in list(logger.handlers):
    logger.removeHandler(h)

# Create file handler
file_handler = logging.FileHandler("/tmp/sort-balls.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Optional: set a formatter similar to loguru's default
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
