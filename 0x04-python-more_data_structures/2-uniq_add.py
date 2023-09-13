#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    num = 0
    for i in my_set:
        num += i
    return num
