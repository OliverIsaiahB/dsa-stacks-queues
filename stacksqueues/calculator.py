"""Evaluate an arithmetic expression with +, -, *, / and precedence, using the
classic TWO-STACK method: one stack for numbers, one for operators."""
from __future__ import annotations

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}


def tokenize(expr: str) -> list[str]:
    """Split into number and operator tokens, ignoring spaces."""
    tokens: list[str] = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch.isspace():
            i += 1
        elif ch.isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            tokens.append(expr[i:j])     # a multi-digit number
            i = j
        else:
            tokens.append(ch)            # a single operator char
            i += 1
    return tokens


def _apply(operators: list[str], operands: list[int]) -> None:
    """Pop one operator and two operands, apply, push the result back."""
    op = operators.pop()
    right = operands.pop()
    left = operands.pop()
    if op == "+":
        operands.append(left + right)
    elif op == "-":
        operands.append(left - right)
    elif op == "*":
        operands.append(left * right)
    else:
        operands.append(int(left / right))   # truncate toward zero


def evaluate(expr: str) -> int:
    """Evaluate expr respecting * / over + - precedence."""
    operands: list[int] = []             # the number stack
    operators: list[str] = []            # the operator stack
    for tok in tokenize(expr):
        if tok.isdigit():
            operands.append(int(tok))
        else:
            # apply any pending operators of >= precedence first
            while operators and PRECEDENCE[operators[-1]] >= PRECEDENCE[tok]:
                _apply(operators, operands)
            operators.append(tok)
    while operators:                     # drain the rest
        _apply(operators, operands)
    return operands[-1]
