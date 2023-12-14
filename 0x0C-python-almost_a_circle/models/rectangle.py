#!/usr/bin/python3
"""Module that defines a class Rectangle
that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """
    class that inherits from Base and create Rectangle
    with some cords
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__class__.checker("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__class__.checker("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__class__.checker("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__class__.checker("y", value)
        self.__y = value

    @staticmethod
    def checker(name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        w = self.width
        h = self.height
        y = self.y
        ed = self.id
        x = self.x
        cls = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}".format(cls, ed, x, y, w, h)
