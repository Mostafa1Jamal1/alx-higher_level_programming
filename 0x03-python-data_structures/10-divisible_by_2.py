#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_list = []
    for i in my_list:
        is_list.append(True if i % 2 == 0 else False)
    return is_list
