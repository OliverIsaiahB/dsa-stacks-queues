import pytest
from stacksqueues.stack import Stack


def test_push_pop_is_lifo():
    s = Stack()
    s.push(1); s.push(2); s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_peek_does_not_remove():
    s = Stack()
    s.push(42)
    assert s.peek() == 42
    assert len(s) == 1


def test_pop_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
