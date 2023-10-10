#!/usr/bin/python3
'''Module of only one class Student'''


class Student:
    '''Defines a student by:
    Public instance attributes:
        first_name, last_name, age
    '''
    def __init__(self, first_name, last_name, age):
        '''Instantiation with first_name, last_name and age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary representation of a Student instance'''
        return self.__dict__
