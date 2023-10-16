#!/usr/bin/python3
'''Module of the Square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class defines square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Class constructor'''
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        '''return [Square] (<id>) <x>/<y> - <size>'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
    
    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size'''
        self.width = value
        self.height = value
