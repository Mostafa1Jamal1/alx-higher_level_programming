#!/usr/bin/python3
'''This module of only one function -> lookup(obj)'''


def lookup(obj):
    '''This function returns the list of
    available attributes and methods of an object.'''
    return dir(obj)
