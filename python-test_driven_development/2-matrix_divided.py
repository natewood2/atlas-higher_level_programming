#!/usr/bin/python3
""" Defines the module """


def matrix_divided(matrix, div):
    """ The function of the program """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    rows_error = "Each row of the matrix must have the same size"
    div_error = "div must be a number"
    divide_by_zero_error = "division by zero"
    
    
    if not isinstance(matrix, list):
        raise TypeError(matrix_error)
    if not isinstance(div, (int, float)):
        raise TypeError(div_error)
    if div == 0:
        raise ZeroDivisionError(divide_by_zero_error)
    
    if len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
            raise TypeError(matrix_error)
    row_length = len(matrix[0])
    
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(rows_error)
        
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(matrix_error)
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return new_matrix