#!/usr/bin/python3
'''module of only one function save_to_json_file(my_obj, filename)'''


import json


def save_to_json_file(my_obj, filename):
    '''writes an Object to a text file, using a JSON representation
    exceptions if the object can’t be serialized
    and permissions are not managed'''
    with open(filename, mode='w', encoding='utf-8') as afile:
        json_rep = json.dumps(my_obj)
        return afile.write(json_rep)
