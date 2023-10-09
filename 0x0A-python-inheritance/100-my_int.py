#!/usr/bin/python3
'''module of only one class MyInt'''


class MyInt(int):
    '''MyInt is a rebel. MyInt has == and != operators inverted'''

    def __eq__(self, value):
        '''Return self != value.'''
        return super().__ne__(value)

    def __ne__(self, value):
        ''' Return self == value.'''
        return super().__eq__(value)
