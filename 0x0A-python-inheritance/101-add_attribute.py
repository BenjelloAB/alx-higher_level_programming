#!/usr/bin/python3
"""A Module which defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """method that add a new attr if possible

    Args:
        obj (any): The object to add an attribute to
        att (str): The name of the attribute
        value (any): The value of attribute
    Raises:
        TypeError: If the attribute cannot be added for some reason
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
