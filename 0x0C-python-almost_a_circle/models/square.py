#!/usr/bin/python3
"""Module that defines Square class which
inherit from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class , a subclass of Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        s = self.height
        ed = self.id
        x = self.x
        y = self.y
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(ed, x, y, s)
