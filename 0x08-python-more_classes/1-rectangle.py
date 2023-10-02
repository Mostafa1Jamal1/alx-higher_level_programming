#!/usr/bin/python3
'''This module is very simple with only one class that defines a rectangle'''


class Rectangle:
    '''There is two private attributes width, height'''

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        '''The getter of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''The setter of width
        the value must be an integer and >= 0'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Return height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the value of height
        the value must be an integer and >= 0'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
