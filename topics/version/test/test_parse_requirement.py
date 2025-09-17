import operator

import pytest

from versionlib import parse_requirement


@pytest.mark.parametrize(
    "requirement,expected",
    [
        pytest.param("> 1.5.3", (operator.gt, (1, 5, 3)), id=">1.5.3"),
        pytest.param(">= 1.5.3", (operator.ge, (1, 5, 3)), id=">=1.5.3"),
        pytest.param("== 1.5.3", (operator.eq, (1, 5, 3)), id="==1.5.3"),
        pytest.param("> 1.5.X", (operator.gt, (1, 5, "x")), id=">1.5.X"),
        pytest.param(">= 1.5.X", (operator.ge, (1, 5, "x")), id=">=1.5.X"),
        pytest.param("== 1.5.X", (operator.eq, (1, 5, "x")), id="==1.5.X"),
    ],
)
def test_parse_requirement(requirement, expected):
    assert parse_requirement(requirement) == expected
