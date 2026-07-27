"""Balanced-parentheses is THE canonical stack problem. Brackets must close in
reverse order of opening — exactly the LIFO discipline a stack enforces."""
from __future__ import annotations

from stacksqueues.stack import Stack

PAIRS = {")": "(", "]": "[", "}": "{"}   # closer -> required opener


def is_balanced(s: str) -> bool:
    """Return True if every bracket in s is correctly matched and nested."""
    stack = Stack()
    for ch in s:
        if ch in "([{":                  # an opener: remember it
            stack.push(ch)
        elif ch in ")]}":                # a closer: it must match the top
            if stack.is_empty():         # closer with nothing open -> unbalanced
                return False
            if stack.pop() != PAIRS[ch]: # wrong kind of opener on top
                return False
        # any other character is ignored
    return stack.is_empty()              # leftover openers -> unbalanced
