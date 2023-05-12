#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            # print each integer followed by a space
            print("{:d}".format(num), end="")
            if i != len(row) - 1:
                # add a space after each integer except for the last one in the row
                print(" ", end="")
        print()
