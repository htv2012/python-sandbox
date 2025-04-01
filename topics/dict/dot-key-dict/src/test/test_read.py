import pytest
from dot_key_dict import DotKeyDict


@pytest.fixture(scope="module")
def sample():
    return DotKeyDict(
        {
            "metadata": {
                "name": "env1",
                "description": "My first environment",
                "tags": ["t0", "t1", "t2"],
            },
            "lookup": {"0": "zero"},
        }
    )


def test_name(sample):
    assert sample["metadata.name"] == "env1"


def test_description(sample):
    assert sample["metadata.description"] == "My first environment"


def test_tag(sample):
    assert sample["metadata.tags"] == ["t0", "t1", "t2"]


def test_list_index(sample):
    assert sample["metadata.tags.0"] == "t0"


def test_numeric_key_found(sample):
    assert sample["lookup.0"] == "zero"


def test_numeric_key_not_found(sample):
    assert "lookup.1" not in sample
