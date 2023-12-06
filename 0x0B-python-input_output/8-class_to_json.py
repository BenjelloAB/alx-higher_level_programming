#!/usr/bin/python3
'''function that returns the dictionary description of an object'''


def class_to_json(obj):
    '''method class_to_json
       returns builds a dictionary
    '''
    return obj.__dict__
