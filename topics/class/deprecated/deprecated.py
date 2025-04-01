import functools
import logging
import warnings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
warnings.simplefilter("always")


def deprecated_function(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        warnings.warn(
            "Function is deprecated",
            category=DeprecationWarning,
            stacklevel=2,
        )
        return function(*args, **kwargs)

    return wrapper


def deprecated_class(klass):
    for name, func in list(vars(klass).items()):
        if name.startswith("_"):
            continue
        if not callable(func):
            continue
        # logger.debug('Callable: %s', name)
        setattr(klass, name, deprecated_function(func))

    return klass
