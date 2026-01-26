import abc
import logging
import threading
from typing import Optional

logger = logging.getLogger(__name__)


class PeriodicTask(abc.ABC):
    """
    An abstract base class that triggers a recurring action in a background thread.

    This class manages a daemon thread that executes the `on_timeout` method
    every `duration_sec` seconds. It is designed for synchronous environments
    (like scripts using time.sleep) where background work must happen
    without blocking the main execution thread.

    Args:
        duration_sec (int): Seconds to wait between each execution of on_timeout.

    Detailed Usage:
        1. Subclass `PeriodicTask` and implement `on_timeout`.
        2. Instantiate with a `duration_sec` in seconds.
        3. Call `start()` to launch the background execution.
        4. Call `stop()` to cleanly terminate the background thread.

    Example:
        class FileChecker(PeriodicTask):
            def on_timeout(self):
                print("Checking for file changes...")

        task = FileChecker(duration_sec=60)
        task.start()
        # ... main loop ...
        task.stop()
    """

    @abc.abstractmethod
    def on_timeout(self):
        """
        The action to perform every 'duration_sec' seconds.

        This is the primary method to implement in your subclass.
        It runs in a separate background thread.
        """
        pass

    def __init__(self, duration_sec: int):
        self.duration_sec = duration_sec
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    def start(self):
        """
        Start the background thread.

        Does nothing if the thread is already running. The thread is
        marked as a daemon so it will exit when the main script ends.
        """
        if self._thread is not None and self._thread.is_alive():
            return  # Thread is already running

        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        """
        Stop the background thread.

        Signals the thread to exit and joins it to ensure cleanup.
        """
        if self._thread:
            self._stop_event.set()
            logger.debug("stopping")
            self._thread.join(timeout=5.0)
            logger.debug("stopped")
            self._thread = None

    def _run(self):
        """
        Internal loop managing the timing logic.

        The loop uses the stop event's wait mechanism to sleep efficiently
        while remaining responsive to a stop signal.
        """
        while not self._stop_event.is_set():
            # wait() returns True if the event is set, False if it times out
            stopped = self._stop_event.wait(timeout=self.duration_sec)
            if not stopped:
                self.on_timeout()

        logger.debug("Exit timer loop")
