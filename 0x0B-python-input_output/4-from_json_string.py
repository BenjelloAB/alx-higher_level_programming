#!/usr/bin/python3
'''Module that defines a function which deserialize data to JSON strings'''
import json


def from_json_string(my_str):
    '''
    function that deserialize an object

    Args:
        my_obj: a Python object of any type
    '''
    return json.loads(my_str)
