#!/usr/bin/python3
'''This module of only one class MyList'''


class MyList(list):
    '''This class inherts from list class'''

    def print_sorted(self):
        '''prints the list, but sorted (ascending sort)'''
        __copy_list = self[:]
        __copy_list.sort()
        print(__copy_list)
