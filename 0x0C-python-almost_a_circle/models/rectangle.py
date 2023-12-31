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
        """
        initialize the instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
            Returning the private width attr
        '''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''
        Setting the private width attr
        '''
        self.__class__.checker2("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            Returning the private height attr
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setting the private height attr
        '''
        self.__class__.checker2("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            getting the private attribute x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            setting the private attribute x
        '''
        self.__class__.checker1("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            returning the private attribute y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Setting the private attribute y
        '''
        self.__class__.checker1("y", value)
        self.__y = value

    @staticmethod
    def checker1(name, value):
        """
        checker 1
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def checker2(name, value):
        """
            checker 2
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''
           Calculates the area of the recatangle
        '''
        return self.width * self.height

    def display(self):
        '''
            Prints a representation of the rectangle
        '''
        for k in range(self.y):
            print()
        for i in range(self.height):
            for z in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''
            Overwriting the string method
        '''
        w = self.width
        h = self.height
        y = self.y
        ed = self.id
        x = self.x
        cls = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}".format(cls, ed, x, y, w, h)

    def update(self, *args, **kwargs):
        '''
            updates values
        '''
        if len(args) != 0:
            if len(args) > 0 and args[0] is not None:
                self.id = args[0]
            if len(args) > 1 and args[1] is not None:
                self.width = args[1]
            if len(args) > 2 and args[2] is not None:
                self.height = args[2]
            if len(args) > 3 and args[3] is not None:
                self.x = args[3]
            if len(args) > 4 and args[4] is not None:
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
                if k == "id":
                    self.id = v

    def to_dictionary(self):
        """
        Returns a dictionary representation of the object
        """
        dic = {}
        dic['x'] = self.x
        dic['y'] = self.y
        dic['id'] = self.id
        dic['height'] = self.height
        dic['width'] = self.width
        return dic
