#!/usr/bin/python3
"""
Module that defines a square printing function
"""


def print_square(size):
    """
    a function that prints a square of size cols
    and size rows

    Args:
        size : the length of the square

    Raises:
        TypeError:   if the size is not an integer
        TypeError: if size is a float or is less than 0
        ValueError: when size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
