import functools
import inspect
from collections import Sequence, Set


def validate_value(value, valid_values, error_message=None):
    if error_message is None:
        error_message = "Validation failed: {!r} is not in {}".format(
            value, valid_values
        )

    # If valid value is not a set nor a sequence,
    # we assume it is an "enum" class
    if not isinstance(valid_values, (Sequence, Set)):
        valid_values = set(
            getattr(valid_values, attribute)
            for attribute in dir(valid_values)
            if not attribute.startswith("_")
        )

    if value not in valid_values:
        raise ValueError(error_message)


def validate_parameters(**parameters):
    def outter(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            callargs = inspect.getcallargs(func, *args, **kwargs)
            invalid_keys = parameters.keys() - callargs.keys()

            if invalid_keys:
                template = "Function {!r} does not have a parameter(s) named {}"
                error_message = template.format(func.__name__, ", ".join(invalid_keys))
                raise LookupError(error_message)

            for parameter_name, enum_class in list(parameters.items()):
                value = callargs[parameter_name]
                validate_value(value, enum_class)

            return func(*args, **kwargs)

        return inner

    return outter
