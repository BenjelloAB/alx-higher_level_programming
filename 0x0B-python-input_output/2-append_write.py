#!/usr/bin/python3
'''This module defines a method that write and append a string to a file'''


def append_write(filename="", text=""):
    """
    This function write some text to a file

    Args:
        filename: the file name
        text: string to write into the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        chars = f.write(text)
    return chars
