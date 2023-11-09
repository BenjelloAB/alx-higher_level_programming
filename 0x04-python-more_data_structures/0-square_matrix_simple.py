#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    copy = matrix[:]
    new_matrix = []
    for i in range(len(copy)):
        temp = []
        for j in range(len(copy[i])):
            temp.append(copy[i][j] * copy[i][j])
        new_matrix.append(temp)
    return new_matrix
