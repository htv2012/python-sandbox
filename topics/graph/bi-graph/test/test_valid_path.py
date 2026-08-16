import pytest

COMPLEX = [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 7],
    [3, 8],
    [4, 9],
    [4, 10],
    [10, 11],
]


@pytest.mark.parametrize(
    ["edges", "source", "destination", "expected"],
    [
        pytest.param([[0, 1], [1, 2], [2, 0]], 0, 2, True, id="example 1"),
        pytest.param(
            [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False, id="example 2"
        ),
        pytest.param(
            [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 1, 2, True, id="example 2-true"
        ),
        pytest.param(COMPLEX, 1, 11, True, id="complex 1-11"),
    ],
)
def test_valid_path(graph, edges, source, destination, expected):
    for edge in edges:
        graph.add_edge(*edge)

    assert graph.valid_path(source, destination) is expected
