#!/usr/bin/python3
'''Module of only one function pascal_triangle(n)'''


def pascal_triangle(n):
    '''returns a list of lists of integers
    representing the Pascal’s triangle of n'''

    pascalist = []

    if n <= 0:
        return pascalist

    for row in range(n):
        rowlist = [1]

        for ele in range(row):

            if ele == (row - 1):
                rowlist.append(1)
            else:
                prev_ele1 = pascalist[row - 1][ele]
                prev_ele2 = pascalist[row - 1][ele + 1]
                rowlist.append(prev_ele1 + prev_ele2)

        pascalist.append(rowlist)

    return pascalist
