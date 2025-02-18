import pytest

from dot_key_dict import DotKeyDict


@pytest.fixture
def sample():
    return DotKeyDict(
        {"metadata": {"name": "env1", "description": "My first environment"}}
    )


def test_with_dot(sample):
    sample["metadata.name"] = "env2"
    assert sample["metadata.name"] == "env2"
    assert sample["metadata"]["name"] == "env2"


def test_without_dot(sample):
    sample["metadata"]["name"] = "env2"
    assert sample["metadata.name"] == "env2"
    assert sample["metadata"]["name"] == "env2"


def test_write_new(sample):
    assert "payload.key" not in sample
    sample["payload.key"] = 1190

    assert "payload.key" in sample
    assert sample["payload.key"] == 1190
