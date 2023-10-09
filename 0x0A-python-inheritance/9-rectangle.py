#!/usr/bin/python3
'''Module of one class Rectangle that inherts from BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass from BaseGeometry that:
    Instantiation with width and height'''

    def __init__(self, width, height):
        '''Instantiation with width and height'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''return, the following rectangle description:
        [Rectangle] <width>/<height>'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        '''Returns the area of the Rectangle'''
        return self.__width * self.__height
