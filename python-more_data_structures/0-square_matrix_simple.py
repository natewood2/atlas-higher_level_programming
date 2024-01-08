#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_r = []
        for num in row:
            squared_r.append(num ** 2)
        squared_matrix.append(squared_r)
    return squared_matrix
