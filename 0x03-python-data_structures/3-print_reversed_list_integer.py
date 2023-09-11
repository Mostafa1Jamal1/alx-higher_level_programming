#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = list(range(len(my_list)))
    n.reverse()
    for i in n:
        print("{}".format(my_list[i]))
