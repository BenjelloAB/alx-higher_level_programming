#!/usr/bin/python3
"""real definition of recatangle"""


class Rectangle:
    """
     defining the width and height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): the width of the rectangle
            height (int) :the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the width of the rectangle

        Returns:
        int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle

        Args:
        value (int): the new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle

        Returns:
        int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the width of the rectangle

        Args:
            value (int): the new height value
        """
        if value < 0:
            raise ValueError("height must be an integer")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
