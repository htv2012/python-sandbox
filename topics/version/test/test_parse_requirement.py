import operator

import pytest

from versionlib import Version, parse_requirement


@pytest.mark.parametrize(
    "requirement,expected",
    [
        pytest.param("> 1.5.3", (operator.gt, Version("1.5.3")), id=">1.5.3"),
        pytest.param(">= 1.5.3", (operator.ge, Version("1.5.3")), id=">=1.5.3"),
        pytest.param("== 1.5.3", (operator.eq, Version("1.5.3")), id="==1.5.3"),
        pytest.param("> 1.5.X", (operator.gt, Version("1.5.x")), id=">1.5.X"),
        pytest.param(">= 1.5.X", (operator.ge, Version("1.5.x")), id=">=1.5.X"),
        pytest.param("== 1.5.X", (operator.eq, Version("1.5.x")), id="==1.5.X"),
        pytest.param("1.5.X", (operator.eq, Version("1.5.x")), id="1.5.X"),
    ],
)
def test_parse_requirement(requirement, expected):
    assert parse_requirement(requirement) == expected
