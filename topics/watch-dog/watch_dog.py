import abc
import logging
import threading


logger = logging.getLogger(__name__)


class WatchDog(abc.ABC):
    def __init__(self, duration: int, job, args, kwargs):
        self.duration = duration
        self.job = job
        self.args = args
        self.kwargs = kwargs

        self.timer = None
        self._lock = threading.Lock()

    def start(self):
        """Start the watchdog."""
        with self._lock:
            if self.timer is None:
                self._schedule_timer()

    def stop(self):
        """Stop the watchdog."""
        with self._lock:
            if self.timer:
                self.timer.cancel()
                self.timer = None

    def reset(self):
        """Reset the watchdog timer."""
        with self._lock:
            if self.timer:
                self.timer.cancel()
            self._schedule_timer()

    def _schedule_timer(self):
        """Internal helper to schedule the next timeout."""
        self.timer = threading.Timer(self.duration, self._timeout_handler)
        self.timer.daemon = True # Allows script to exit even if timer is running
        self.timer.start()

    def _timeout_handler(self):
        """Logic executed when timer expires."""
        self.job(*self.args, **self.kwargs)
        # To make it a recurring watchdog like your previous version:
        self.timer = None
        self.start()
