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
        """ overriding the str method
        """
        s = self.width
        ed = self.id
        x = self.x
        y = self.y
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(ed, x, y, s)

    @property
    def size(self):
        """
        getter for the size attr
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for the size attr
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the square attributes
        """

        if len(args) > 0:
            if len(args) > 0 and args[0] is not None:
                self.id = args[0]
            if len(args) > 1 and args[1] is not None:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2 and args[2] is not None:
                self.x = args[2]
            if len(args) > 3 and args[3] is not None:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k) is True:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the object
        """
        dic = {}
        dic['id'] = self.id
        dic['size'] = self.width
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
