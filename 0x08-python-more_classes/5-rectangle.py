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

    def __str__(self):
        string = ""
        if self.__width == 0:
            return string
        for row in range(self.__height):
            string += "#" * self.__width
            if row != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.height)

    def __del__(self):
        print("Bye rectangle...")

    def area(self):
        '''returns the rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns the rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

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
