#!/usr/bin/python3

"""Square class"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the obj

        Args:
            size (int): The size of the square
            position (int, int): position of the new sqr
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter for position field"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter for the position field

        Args:
            value (int, int): position tuple
        """
        if(not type(value) is tuple or
                len(value) != 2 or
                not all(type(num) == int for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square in #"""
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(0, self.__position[1])]

            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
