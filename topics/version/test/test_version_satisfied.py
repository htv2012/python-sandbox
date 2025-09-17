import pytest

from versionlib import Version


@pytest.fixture
def ver():
    return Version("1.5.3")


@pytest.mark.parametrize(
    "requirement,expected",
    [
        (">1.5.2", True),
        (">1.5", True),
        ("1.5.X", True),
        (">=1.5.3", True),
        (">=1.5.x", True),
    ],
)
def test_version_satisfied(ver: Version, requirement, expected):
    assert ver.satisfied(requirement) is expected
