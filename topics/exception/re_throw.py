import logging

logging.basicConfig(level=logging.DEBUG)

try:
    print(x)
except NameError as e:
    # logging.exception(e)
    # logging.info('---')
    logging.error("You need to define this name first")
    e.message = (
        getattr(e, "message", getattr(e, "msg", "")) + "\nYou have to define it first"
    )
    raise
