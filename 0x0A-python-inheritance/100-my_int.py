#!/usr/bin/python3
"""Defines a class MyInt that inherits from int Class"""


class MyInt(int):
    """A Class that inverts int operators == and !="""

    def __eq__(self, value):
        """Overriding == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Overridng != operator with == behavior"""
        return self.real == value
