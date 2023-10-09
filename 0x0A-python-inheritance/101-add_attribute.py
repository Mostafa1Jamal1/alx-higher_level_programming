#!/usr/bin/python3
'''Module of only one function add_attribute'''


def add_attribute(obj, attribute, value):
    '''adds a new attribute to an object if it’s possible.'''
    try:
        setattr(obj, attribute, value)
    except Exception:
        raise TypeError("can't add new attribute")
