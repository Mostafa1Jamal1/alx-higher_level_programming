#!/usr/bin/python3
'''Just class `Square` that defines a square'''


class Square:
    '''In this class
    Private instance attribute: size
    '''

    def __init__(self, size):
        ''' Instantiation with size (no type/value verification)
        Args:
            size: the size of the aquare
        '''
        self.__size = size
