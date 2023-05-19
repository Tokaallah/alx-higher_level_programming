#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[0] * len(row) for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared_value = matrix[i][j] ** 2
            result[i][j] = squared_value

    return (result)
