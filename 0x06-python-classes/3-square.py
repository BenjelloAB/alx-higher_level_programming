#!/usr/bin/python3

"""Square class"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Initialize the obj

        Args:
            size (int): The size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area"""
        return (self.__size * self.__size)
