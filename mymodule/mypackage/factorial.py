""" Provides a function to compute factorial.
"""


def factorial(n):
    """Computes factorial.
    """
    f = 1
    for i in range(n):
        f *= i + 1
    return f
