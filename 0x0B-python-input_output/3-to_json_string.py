#!/usr/bin/python3
'''Module of only one function to_json_string(my_obj)'''

import json


def to_json_string(my_obj):
    '''returns the JSON representation of an object (string)
    exceptions if the object can’t be serialized not handled'''
    return json.dumps(my_obj)
