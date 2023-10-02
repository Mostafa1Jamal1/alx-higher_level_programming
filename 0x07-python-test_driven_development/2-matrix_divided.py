#!/usr/bin/python3
def matrix_divided(matrix, div):
    
    # Check div validation
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    # Check matrix validation
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    # Create new matrix with the result
    new_matrix = []
    for i, row in enumerate(matrix):
        if type(row) != list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        new_matrix.append([])
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            else:
                new_matrix[i].append(round((item / div), 2))

    return new_matrix

