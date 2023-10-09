#!/usr/bin/python3
'''Module of one class BaseGeometry'''


class BaseGeometry:
    '''A class with only one public instance method:
        def area(self): that raises an Exception with the message
        area() is not implemented'''

    def area(self):
        '''raises an Exception with the message area() is not implemented'''
        raise Exception('area() is not implemented')
