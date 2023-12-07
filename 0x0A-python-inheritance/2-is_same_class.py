#!/usr/bin/python3
"""Module that defines a class-checking function"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class

    Args:
        obj: The object to check
        a_class: The class to match the type of the object to
    """
    if type(obj) == a_class:
        return True
    return False
