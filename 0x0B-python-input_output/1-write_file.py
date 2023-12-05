#!/usr/bin/python3
'''This module defines a method that write a string to a file'''


def write_file(filename="", text=""):
    """
    This function write some text to a file

    Args:
        filename: the file name
        text: string to write into the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        chars = f.write(text)
    return chars
