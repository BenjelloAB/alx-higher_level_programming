#!/usr/bin/python3
"""This module defines a method that reads from a file"""


def read_file(filename=""):
    """
    Function that reads from a filename

    Args:
        filename: the file name string
    """
    with open(filename, "r") as f:
        lines = f.read()
    print(lines, end="")
