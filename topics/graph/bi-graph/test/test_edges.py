def test_add_edge(graph):
    graph.add_edge(1, 2)
    assert graph.edges == {(1, 2)}
    assert graph.nodes == {1, 2}

    graph.add_edge(1, 3)
    assert graph.edges == {(1, 2), (1, 3)}
    assert graph.nodes == {1, 2, 3}
