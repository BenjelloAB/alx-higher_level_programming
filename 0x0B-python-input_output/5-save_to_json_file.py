#!/usr/bin/python3
'''Module that defines a function which serialize data
to JSON strings into a file'''
import json


def save_to_json_file(my_obj, filename):
    '''
    function that serializes an object into a json str into a file

    Args:
        my_obj: a Python object of any type
        filename : object file pointing to the fd
    '''
    return json.dump(my_obj, filename)
