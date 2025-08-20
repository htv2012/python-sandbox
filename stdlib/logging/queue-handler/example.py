import logging
from logging.handlers import QueueHandler, QueueListener
from queue import Queue


# Create a queue
log_queue = Queue()

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a handler that writes to a file
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)

# Create a QueueHandler and add it to the root logger
queue_handler = QueueHandler(log_queue)
root = logging.getLogger()
root.addHandler(queue_handler)

# Create a QueueListener to handle the log records in the queue
queue_listener = QueueListener(log_queue, file_handler)
queue_listener.start()

# Now, let's log some messages
logging.info('This is an info message')
logging.warning('This is a warning message')

# Stop the QueueListener when done
queue_listener.stop()