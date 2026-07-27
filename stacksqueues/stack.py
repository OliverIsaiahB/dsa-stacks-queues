"""A stack is a LIFO collection: the Last thing In is the First thing Out.
A Python list already supports O(1) append and pop from the end, so we wrap
one to expose a clean, intention-revealing stack API."""
from __future__ import annotations


class Stack:
    def __init__(self) -> None:
        self._items: list[int] = []      # the top of the stack is the END of the list

    def push(self, value: int) -> None:
        """Add to the top. list.append is amortized O(1)."""
        self._items.append(value)

    def pop(self) -> int:
        """Remove and return the top. Raises if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()         # pop() with no index removes the END: O(1)

    def peek(self) -> int:
        """Look at the top without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)
