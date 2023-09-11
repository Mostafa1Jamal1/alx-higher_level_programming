#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a_list in matrix:
        for i in range(len(a_list)):
            print("{:d}".format(a_list[i]), end="")
            if i < (len(a_list) - 1):
                print(" ", end="")
        print()
