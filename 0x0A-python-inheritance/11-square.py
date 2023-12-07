!/usr/bin/python3
"""
Improving the previous Square Class
"""


PrevSquare = __import__('10-square').Square


class Square(PrevSquare):
    """
    Improving Class Square
    """

    def __init__(self, size):
        """Constructor"""
        super().__init__(size)

    def __str__(self):
        """String rep"""
        return '[Square] {0:d}/{0:d}'.format(self.__size)
