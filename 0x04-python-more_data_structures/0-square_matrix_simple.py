#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squar = []
    for alist in matrix:
        squar.append(list((lambda x: x ** 2)(x) for x in alist))
    return squar
