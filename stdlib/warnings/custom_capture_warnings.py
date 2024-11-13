
import warnings
from warnings_tryout import set_level


class CaptureWarning(object):
    def __enter__(self):
        self.original_warning = warnings.warn
        warnings.warn = self.my_warning
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        warnings.warn = self.original_warning
        # Only return True if we wish to suppress the exception

    def my_warning(self, message, category=None, stacklevel=None):
        self.message = message
        self.category = category
        self.stacklevel = stacklevel



if __name__ == '__main__':
    with CaptureWarning() as capture_warning:
        set_level(-4)
        # At this point, the message, category, and stacklevel are in
        # the capture_warning object such as capture_warning.message
