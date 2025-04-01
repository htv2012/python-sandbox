from typing import Union

import pytest
from numericlib import NumericRange


@pytest.fixture(scope="session")
def get_ports():
    """Provide a function which return 1 or more ports."""
    next_port = 50001

    def get_next(count: int = 1) -> Union[int, NumericRange]:
        """Return a single port (int) or a range of ports (NumericRange)."""
        nonlocal next_port

        if count == 1:
            result = next_port
        else:
            result = NumericRange(start=next_port, count=count)

        next_port += count
        return result

    return get_next
