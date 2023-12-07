#!/usr/bin/python3
"""Module that defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """Class rerpresenting base geometry"""

    def area(self):
        """Not yet implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates if a parameter is an integer
        Args:
            name (str): The name of the parameter
            value (int): The parameter to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
