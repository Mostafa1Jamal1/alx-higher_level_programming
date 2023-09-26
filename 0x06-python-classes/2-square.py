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
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
