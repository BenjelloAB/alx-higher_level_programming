#!/usr/bin/python3

"""Square class"""


class Square:
    """Representation of a square"""
    def __init__(self, size=0):
        """Initialize the obj

        Args:
            size (int): The size of the square
        """
        self.__size = size

    def area(self):
        """Calculates the area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the __size value

        Args:
            value (int): the size of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
