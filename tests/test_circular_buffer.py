import pytest
from stacksqueues.circular_buffer import CircularBuffer


def test_fifo_within_capacity():
    b = CircularBuffer(3)
    b.enqueue(1); b.enqueue(2)
    assert b.dequeue() == 1
    assert b.dequeue() == 2


def test_wraparound():
    b = CircularBuffer(2)
    b.enqueue(1); b.enqueue(2)
    assert b.dequeue() == 1
    b.enqueue(3)                 # reuses the slot freed by dequeue
    assert b.dequeue() == 2
    assert b.dequeue() == 3


def test_full_raises():
    b = CircularBuffer(1)
    b.enqueue(1)
    with pytest.raises(OverflowError):
        b.enqueue(2)


def test_empty_raises():
    b = CircularBuffer(1)
    with pytest.raises(IndexError):
        b.dequeue()
