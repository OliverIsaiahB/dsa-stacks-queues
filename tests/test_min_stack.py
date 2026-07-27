import pytest
from stacksqueues.min_stack import MinStack


def test_min_tracks():
    s = MinStack()
    s.push(3); assert s.get_min() == 3
    s.push(5); assert s.get_min() == 3
    s.push(2); assert s.get_min() == 2


def test_min_restores_after_pop():
    s = MinStack()
    s.push(3); s.push(2)
    assert s.get_min() == 2
    s.pop()
    assert s.get_min() == 3


def test_empty_min_raises():
    s = MinStack()
    with pytest.raises(IndexError):
        s.get_min()
