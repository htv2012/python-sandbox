import pytest

from camel import camel2snake


@pytest.mark.parametrize(
    "text,expected",
    [
        pytest.param("HappyPath", "happy_path", id="happy path"),
        pytest.param("IBMPcJr", "ibm_pc_jr", id="all caps the the beginning"),
        pytest.param("CheckIDStation", "check_id_station", id="all caps in the middle"),
        pytest.param("PerformPOST", "perform_post", id="all caps at the end"),
    ],
)
def test_camel(text, expected):
    assert camel2snake(text) == expected
