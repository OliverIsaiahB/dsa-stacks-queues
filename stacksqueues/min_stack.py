"""A MinStack supports push, pop, and get_min — all in O(1). The trick: store
with each value the minimum of the stack AT THE TIME it was pushed, so the top
always carries the current minimum."""
from __future__ import annotations


class MinStack:
    def __init__(self) -> None:
        # each entry is (value, min-so-far including this value)
        self._stack: list[tuple[int, int]] = []

    def push(self, value: int) -> None:
        current_min = value if not self._stack else min(value, self._stack[-1][1])
        self._stack.append((value, current_min))

    def pop(self) -> int:
        if not self._stack:
            raise IndexError("pop from empty stack")
        return self._stack.pop()[0]

    def top(self) -> int:
        if not self._stack:
            raise IndexError("top from empty stack")
        return self._stack[-1][0]

    def get_min(self) -> int:
        """The current minimum, in O(1): it's stored at the top."""
        if not self._stack:
            raise IndexError("get_min from empty stack")
        return self._stack[-1][1]

    def __len__(self) -> int:
        return len(self._stack)
