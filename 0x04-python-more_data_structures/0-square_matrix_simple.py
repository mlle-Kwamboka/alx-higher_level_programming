#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New_matrix = []
    for row in matrix:
        for col in row:
            New_matrix = list(map(lambda col: col**2))
            return New_matrix
