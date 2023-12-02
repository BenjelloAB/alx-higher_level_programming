#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' delimiters

    Args:
        text: The str text

    Raises:
        TypeError: If text is not a str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
