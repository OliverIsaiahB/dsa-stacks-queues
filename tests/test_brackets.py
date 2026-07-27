from stacksqueues.brackets import is_balanced


def test_simple_balanced():
    assert is_balanced("()") is True
    assert is_balanced("([]{})") is True


def test_nested():
    assert is_balanced("{[()]}") is True


def test_unbalanced():
    assert is_balanced("(]") is False
    assert is_balanced("(()") is False
    assert is_balanced("())") is False


def test_empty_is_balanced():
    assert is_balanced("") is True


def test_ignores_other_chars():
    assert is_balanced("a(b[c]d)e") is True
