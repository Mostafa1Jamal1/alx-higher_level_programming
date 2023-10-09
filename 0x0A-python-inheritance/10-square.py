#!/usr/bin/python3
'''Module of Square class that inherits from Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A class that defines a Square'''

    def __init__(self, size):
        '''Instantiation size'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
