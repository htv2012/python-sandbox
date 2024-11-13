import logging
import sys


def fut():
    """Function under test."""
    print("Hello")
    print("Warning: out of coffee", file=sys.stderr)


def test_fut(capfd):
    # Act
    fut()
    cap = capfd.readouterr()
    logging.debug("fut() produces stdout=%r", cap.out)
    logging.debug("fut() produces stderr=%r", cap.err)

    # Verify
    assert cap.out == "Hello\n"
    assert cap.err == "Warning: out of coffee\n"
