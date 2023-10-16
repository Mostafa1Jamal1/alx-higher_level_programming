#!/usr/bin/python3
'''Model of the base class'''


import json


class Base:
    '''The base class of all of the classes in this project'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Instantiating the id and increament nb_objects'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])
