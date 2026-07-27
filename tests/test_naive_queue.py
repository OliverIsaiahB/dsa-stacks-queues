import pytest
from stacksqueues.naive_queue import NaiveQueue


def test_fifo_order():
    q = NaiveQueue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_dequeue_empty_raises():
    q = NaiveQueue()
    with pytest.raises(IndexError):
        q.dequeue()
