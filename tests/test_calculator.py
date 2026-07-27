from stacksqueues.calculator import tokenize, evaluate


def test_tokenize_multidigit():
    assert tokenize("12 + 3") == ["12", "+", "3"]


def test_addition():
    assert evaluate("1 + 2 + 3") == 6


def test_precedence():
    assert evaluate("2 + 3 * 4") == 14       # not 20
    assert evaluate("2 * 3 + 4") == 10


def test_subtraction_left_to_right():
    assert evaluate("10 - 3 - 2") == 5


def test_division_truncates():
    assert evaluate("7 / 2") == 3
