#!/usr/bin/python3
"""
    Integer addition function
    Floats are converted to integers
"""


def add_integer(a, b=98):
    """
        defines an integer adding function
    """
    if (not isinstance(a, float)) and (not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
