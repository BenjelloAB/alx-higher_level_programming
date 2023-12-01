#!/usr/bin/python3
"""
    A module defining a function that divide all matrix elems
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix

        Args:
            matrix : 2d list of elements
            div : the divider number

        Raises:
            TypeError (1): if the elements aren't floats or ints
            TypeError (2): if the rows aren't equal size wise
            TypeError (3): if the div is not an int or float type
            ZeroDivisionError: if we are dividing by 0
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    str = "matrix must be a matrix (list of lists) of integers/floats"

    if len(matrix) == 0:
        raise TypeError(str)
    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            raise TypeError(str)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError(str)

    row_len = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    sub_list = []
    for i in range(len(matrix)):
        for j in range(row_len):
            res = round(matrix[i][j] / div, 2)
            sub_list.append(res)
        new_matrix.append(sub_list)
        sub_list = []
    return new_matrix
