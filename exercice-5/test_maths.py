import pytest
def add(x, y):
    """Addition function."""
    return x + y

def subtract(x, y):
    """Subtraction function."""
    return x - y

def multiply(x, y):
    """Multiplication function."""
    return x * y

def divide(x, y):
    """Division function."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

"""écrire les tests unitaires pour ces fonctions.
atteindre un coverage de 100%
"""

def test_add():
    assert add(3, 4) == 3 + 4
    assert add(-1, 3) == -1 + 3
    assert add(5.5, 5.5) == 5.5 + 5.5

def test_subtract():
    assert subtract(1, 1) == 1 - 1
    assert subtract(-1, 1) == -1 - 1
    assert subtract(3, 7) == 3 - 7
    assert subtract(7, 3) == 7 - 3

def test_multiply():
    assert multiply(0, 0) == 0 * 0
    assert multiply(1, 1) == 1 * 1
    assert multiply(3, 7) == 3 * 7
    assert multiply(3, 0.5) == 3 * 0.5

def test_divide():
    assert divide(1, 1) == 1 / 1
    assert divide(0, 1) == 0 / 1
    with pytest.raises(ValueError):
        divide(1, 0)
    assert divide(20, 10) == 20 / 10