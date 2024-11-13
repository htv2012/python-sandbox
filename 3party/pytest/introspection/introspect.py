import inspect
import logging


def explore(obj, label: str):
    logging.info("%s: %r", label, obj)
    for name in sorted(dir(obj)):
        if name.startswith("_"):
            continue
        value = getattr(obj, name)
        if callable(value):
            logging.info("- %s%s", name, inspect.signature(value))
            doc = inspect.getdoc(value)
            if doc:
                first = doc.splitlines()[0]
                logging.info("  %s", first)
        else:
            logging.info("- %s: %r", name, value)
        logging.info("")
