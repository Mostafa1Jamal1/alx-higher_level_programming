#!/usr/bin/python3
'''Module of only one function load_from_json_file(filename)'''


import json


def load_from_json_file(filename):
    '''creates an Object from a “JSON file”
    exceptions if the JSON string doesn’t represent an object
    and file permissions / exceptions are not managed'''
    with open(filename, encoding="utf-8") as afile:
        return json.loads(afile.read())
