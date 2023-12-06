#!/usr/bin/python3
'''Module that defines a function which deserialize JSON strings
from a file into python object of some type'''
import json


def load_from_json_file(filename):
    '''
    function that serializes a json string from a file into an obj

    Args:
        filename : object file pointing to the fd
    '''
    with open(filename, "r") as f:
        return json.load(f)
