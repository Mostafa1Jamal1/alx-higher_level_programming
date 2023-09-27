#!/usr/bin/python3
'''Just class `Square` that defines a square'''


class Square:
    '''In this class
    Private instance attribute: size
    '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Instantiation with size optional
        Args:
            size (int): the size of the aquare, must be >= 0
            position (tuple): a tuple of 2 positive integers
        '''
        self.size = size
        self.position = position

    def area(self):
        '''Get the area of the square

        Returns:
            the area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        '''Print the area of the square object with #s'''
        for i in range(self.__size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end="")
            print("#" * self.__size)
        if self.__size == 0:
            print()

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

    @property
    def position(self):
        '''position is a tuple of 2 positive integers'''
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if (isinstance(value, tuple) and
                    len(value) == 2 and
                    value[0] >= 0 and
                    value[1] >= 0):
                self.__position = value
            else:
                raise TypeError
        except Exception:
            raise TypeError('position must be a tuple of 2 positive integers')
