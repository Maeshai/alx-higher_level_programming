#!/usr/bin/python3
"""
script define a function for integer addition
"""


def add_integer(a, b=98):
    """
    Return sum of two integers

    Args:
        a (int): First integer
        b (int): Second integer. Optional default value is 98

    Returns:
        int: sum of two integers

    Raises:
        TypeError: If one of args is not integer nor float
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(a, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
