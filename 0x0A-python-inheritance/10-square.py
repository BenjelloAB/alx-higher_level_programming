#!/usr/bin/python3
"""
module that defines a Square class that inherits from
Rectangle that inherits from BG
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiation with a constructor"""
        self.__size = size
        super().__init__(self.__size, self.__size)
