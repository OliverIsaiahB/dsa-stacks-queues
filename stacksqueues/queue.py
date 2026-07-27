"""The FAST queue. collections.deque is a doubly-linked / block structure that
supports O(1) append AND popleft, so dequeue is no longer O(n). Same FIFO
behavior as NaiveQueue, but every operation is amortized O(1)."""
from __future__ import annotations

from collections import deque


class Queue:
    def __init__(self) -> None:
        self._items: deque[int] = deque()

    def enqueue(self, value: int) -> None:
        """Add to the back: O(1)."""
        self._items.append(value)

    def dequeue(self) -> int:
        """Remove and return the front: O(1), because deque.popleft is O(1)."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()     # THE FIX: popleft is O(1), not O(n)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)
