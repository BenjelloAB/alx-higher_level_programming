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
            ZeroDivisionError: if we are dividing by 0
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    str = "matrix must be a matrix (list of lists) of integers/floats"
    for i in range(len(matrix)):
        for j in range(row_len):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError(str)

    new_matrix = []
    sub_list = []
    for i in range(len(matrix)):
        for j in range(row_len):
            res = round(matrix[i][j] / div, 2)
            sub_list.append(res)
        new_matrix.append(sub_list)
        sub_list = []
    return new_matrix
