#!/usr/bin/python3
'''Model of Rectangle class'''


from models.base import Base

class Rectangle(Base):
    '''A class that define width, height, x and y'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiation of width, height, x=0, y=0, id=None'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __validatePosInt(self, name, value, allowzero=True):
        '''Raise Error if value not a positive int'''
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value < 0 and allowzero:
            raise ValueError(name + ' must be >= 0')
        if value <= 0 and not allowzero:
            raise ValueError(name + ' must be > 0')

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.__validatePosInt("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.__validatePosInt("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.__validatePosInt("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.__validatePosInt("y", value)
        self.__y = value

    def __str__(self):
        '''return [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        s = "[Rectangle] " + f"({self.id}) {self.__x}/{self.__y}"
        s = s + f" - {self.__width}/{self.__height}"
        return s

    def area(self):
        '''returns the rectangle area'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        for row in range(self.__height):
            print("#" * self.__width)

