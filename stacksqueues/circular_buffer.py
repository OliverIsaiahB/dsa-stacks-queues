"""A circular (ring) buffer is a fixed-capacity FIFO queue backed by a list whose
indices WRAP using modulo. It reuses slots instead of growing — exactly how
bounded buffers, streaming windows, and hardware queues work."""
from __future__ import annotations


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self._buf: list[int | None] = [None] * capacity
        self._head = 0                   # index of the front element
        self._size = 0                   # number of elements currently stored
        self._capacity = capacity

    def enqueue(self, value: int) -> None:
        if self._size == self._capacity:
            raise OverflowError("buffer is full")
        tail = (self._head + self._size) % self._capacity   # wrap to the start
        self._buf[tail] = value
        self._size += 1

    def dequeue(self) -> int:
        if self._size == 0:
            raise IndexError("dequeue from empty buffer")
        value = self._buf[self._head]
        self._buf[self._head] = None
        self._head = (self._head + 1) % self._capacity      # advance, wrapping
        self._size -= 1
        return value                     # type: ignore[return-value]

    def is_full(self) -> bool:
        return self._size == self._capacity

    def __len__(self) -> int:
        return self._size
