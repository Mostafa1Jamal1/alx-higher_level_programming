#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    over = 0
    sum_all = 0
    for tup in my_list:
        over += tup[1]
        sum_all += tup[0] * tup[1]
    return sum_all / over
