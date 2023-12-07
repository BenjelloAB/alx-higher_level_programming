#!/usr/bin/python3
"""
Improving the previous Square Class
"""


Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """
    Improving Class Square
    """

    def __init__(self, size):
        """Constructor"""
        self.__size = size
        super().__init__(size)

    def __str__(self):
        """String rep"""
        return '[Square] {0:d}/{0:d}'.format(self.__size)
