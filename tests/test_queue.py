import pytest
from stacksqueues.queue import Queue


def test_fifo_order():
    q = Queue()
    for v in (1, 2, 3):
        q.enqueue(v)
    assert [q.dequeue() for _ in range(3)] == [1, 2, 3]


def test_peek():
    q = Queue()
    q.enqueue(7)
    assert q.peek() == 7
    assert len(q) == 1


def test_dequeue_empty_raises():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
