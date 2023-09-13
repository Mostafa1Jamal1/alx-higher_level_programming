#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squar = []
    get_sq = lambda x : x ** 2
    for alist in matrix:
        squar.append(list(get_sq(x) for x in alist))
    return squar
