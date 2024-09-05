# calculator.py

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    if a < 0 or b < 0:
        raise ValueError("Only positive integers are allowed")
    return a + b

def subtract(a: int, b: int) -> int:
    """Return the difference of two integers."""
    if a < 0 or b < 0:
        raise ValueError("Only positive integers are allowed")
    return a - b

def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    if a < 0 or b < 0:
        raise ValueError("Only positive integers are allowed")
    return a * b
