import pytest

from versionlib import Version


@pytest.fixture
def ver():
    return Version("1.5.3")


@pytest.mark.parametrize(
    "requirement,expected",
    [
        pytest.param(">1.5.2", True, id=">1.5.2"),
        # (">1.5", True),
    ],
)
def test_version_satisfied(ver: Version, requirement, expected):
    assert ver.satisfied(requirement) is expected
