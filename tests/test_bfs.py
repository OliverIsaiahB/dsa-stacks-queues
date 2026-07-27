from stacksqueues.bfs import bfs_order, shortest_hops

GRAPH = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}


def test_bfs_visits_all():
    assert sorted(bfs_order(GRAPH, 0)) == [0, 1, 2, 3, 4]


def test_bfs_starts_at_root():
    assert bfs_order(GRAPH, 0)[0] == 0


def test_shortest_hops():
    assert shortest_hops(GRAPH, 0, 4) == 3


def test_same_node():
    assert shortest_hops(GRAPH, 2, 2) == 0


def test_unreachable():
    assert shortest_hops({0: [], 1: []}, 0, 1) == -1
