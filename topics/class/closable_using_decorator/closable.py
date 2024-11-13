import types
import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


AVAILABEL_TAG = "available_after_closed"


def do_not_close(member):
    setattr(member, AVAILABEL_TAG, True)
    return member


def _available_after_closed(member):
    return getattr(member, AVAILABEL_TAG, False)


def _closed(*args, **kwargs):
    raise RuntimeError("Cannot access this method after closed")


def mark_as_closed(instance):
    for attribute_name in dir(instance):
        # Don't mess with dunders
        if attribute_name.startswith("__"):
            continue

        logger.debug("Attribute: %s", attribute_name)
        member = getattr(instance, attribute_name)
        logger.debug("Member: %s", member)
        if callable(member) and not _available_after_closed(member):
            new_obj = types.MethodType(_closed, instance)
            setattr(instance, attribute_name, new_obj)
