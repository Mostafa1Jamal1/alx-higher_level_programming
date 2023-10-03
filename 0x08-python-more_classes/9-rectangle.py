#!/usr/bin/python3
'''This module is very simple with only one class that defines a rectangle'''


class Rectangle:
    '''There is two private attributes width, height
    Attributes:
        number_of_instances (int): number of instances of this class
        print_symbol: Used as symbol for string representation
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        string = ""
        if self.__width == 0:
            return string
        for row in range(self.__height):
            string += str(self.print_symbol) * self.__width
            if row != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        res = rect_1
        if rect_2.area() > rect_1.area():
            res = rect_2
        return res

    @classmethod
    def square(cls, size=0):
        '''returns a new Rectangle instance with width == height == size'''
        return cls(size, size)
