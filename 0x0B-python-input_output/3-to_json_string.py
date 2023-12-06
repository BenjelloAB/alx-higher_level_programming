#!/usr/bin/python3
'''Module that defines a function which serialize data to JSON strings'''
import json


def to_json_string(my_obj):
    '''
    function that serialize an object

    Args:
        my_obj: a Python object of any type
    '''
    return json.dumps(my_obj)
