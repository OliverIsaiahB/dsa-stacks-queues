from stacksqueues.monotonic import next_greater, daily_temperatures


def test_next_greater_basic():
    assert next_greater([2, 1, 3]) == [3, 3, -1]


def test_next_greater_decreasing():
    assert next_greater([5, 4, 3]) == [-1, -1, -1]


def test_next_greater_empty():
    assert next_greater([]) == []


def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 76]) == [1, 1, 2, 1, 0]
