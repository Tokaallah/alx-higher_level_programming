#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0] * len(row) for row in matrix]

    # Iterate over each element in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute the square value of the element
            squared_value = matrix[i][j] ** 2
            # Assign the squared value to the corresponding element in the result matrix
            result[i][j] = squared_value

    return result
