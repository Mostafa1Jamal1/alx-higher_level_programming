#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary)
        key = keys[0]
        num = a_dictionary[key]
        for i in keys:
            if a_dictionary[i] > num:
                key = i
                num = a_dictionary[i]
        return key
