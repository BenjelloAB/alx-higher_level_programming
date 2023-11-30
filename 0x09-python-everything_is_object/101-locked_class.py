#!/usr/bin/python3
"""Defining a locked class"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    unless they are first_name attribute
    """
    __slots__ = ["first_name"]
