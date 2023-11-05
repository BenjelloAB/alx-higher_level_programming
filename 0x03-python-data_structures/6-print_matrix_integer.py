#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        size = len(matrix[i])
        for j in range(0, size):
            el = matrix[i][j]
            print("{:d}{}".format(el, "" if j == size - 1 else " "), end="")
        print()
