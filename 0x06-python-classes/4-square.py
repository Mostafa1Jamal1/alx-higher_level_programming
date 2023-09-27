#!/usr/bin/python3
'''Just class `Square` that defines a square'''


class Square:
    '''In this class
    Private instance attribute: size
    '''

    def __init__(self, size=0):
        ''' Instantiation with size optional
        Args:
            size (int): the size of the aquare, must be >= 0
        '''
        self.size = size

    def area(self):
        '''Get the area of the square

        Returns:
            the area of the square
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''the getter method of class Square
        the size of the aquare, must be >= 0 and of course int type
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
