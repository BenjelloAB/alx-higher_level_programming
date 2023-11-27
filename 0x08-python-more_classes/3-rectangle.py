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
        self.width = width
        self.height = height

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i != self.__height - 1:
                rectangle.append('\n')
        return "".join(rectangle)
