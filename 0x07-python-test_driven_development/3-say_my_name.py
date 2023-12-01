#!/usr/bin/python3
"""
This moduledefines a function that:
prints My name is <first name> <last name>
"""

def say_my_name(first_name, last_name=""):
    """
    a function that prints formatted string with first
    and last names

    Args:
        first_name: string representing first name
        last_name: string representing last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
