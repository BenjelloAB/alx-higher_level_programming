#!/usr/bin/python3
"""Module that defines a Base class"""


class Base:
    """
    A Base class for all the other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
