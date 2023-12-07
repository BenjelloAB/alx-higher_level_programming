#!/usr/bin/python3
''' module that defines a class that defines a
kind checking function
'''


def is_kind_of_class(obj, a_class):
    '''function that checks the kind of an obj
    obj: an object to check for its kind
    a_class: class to match with
    '''
    return isinstance(obj, a_class)
