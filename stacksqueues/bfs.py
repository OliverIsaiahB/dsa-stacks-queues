"""Breadth-first search is the marquee use of a queue. With a FIFO queue, BFS
explores a graph in rings of increasing distance, so it finds the shortest path
(fewest edges) in an UNWEIGHTED graph. This is the queue from earlier in action."""
from __future__ import annotations

from collections import deque

Graph = dict[int, list[int]]


def bfs_order(graph: Graph, start: int) -> list[int]:
    """Return nodes in breadth-first visiting order from start."""
    order: list[int] = []
    visited = {start}                    # never enqueue a node twice
    q: deque[int] = deque([start])
    while q:
        node = q.popleft()               # FIFO: process in discovery order
        order.append(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)            # children go to the BACK of the line
    return order


def shortest_hops(graph: Graph, start: int, goal: int) -> int:
    """Fewest edges from start to goal, or -1 if unreachable."""
    if start == goal:
        return 0
    visited = {start}
    q: deque[tuple[int, int]] = deque([(start, 0)])
    while q:
        node, dist = q.popleft()
        for nbr in graph.get(node, []):
            if nbr == goal:
                return dist + 1          # first arrival = fewest edges
            if nbr not in visited:
                visited.add(nbr)
                q.append((nbr, dist + 1))
    return -1
