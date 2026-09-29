def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# Test the functions
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Division by zero:", divide(10, 0))