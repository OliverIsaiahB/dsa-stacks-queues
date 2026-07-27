"""A queue is FIFO: First In, First Out — like a line at a checkout. This first,
DELIBERATELY NAIVE version stores items in a list and removes from the front.
It is correct but slow; the next step shows why and fixes it."""
from __future__ import annotations


class NaiveQueue:
    def __init__(self) -> None:
        self._items: list[int] = []      # front of the queue is index 0

    def enqueue(self, value: int) -> None:
        """Add to the back. Appending to the end is O(1)."""
        self._items.append(value)

    def dequeue(self) -> int:
        """Remove and return the front. pop(0) shifts every other element: O(n)!"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)        # THE TRAP: removing index 0 is O(n)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)
