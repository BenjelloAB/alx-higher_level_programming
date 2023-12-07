#!/usr/bin/python3
''' module that defines a function to check the parent class of an obj
'''


def inherits_from(obj, a_class):
    '''function that checks if an
    object is an instance of an inherited class

    Args:
    obj: an object to check
    a_class: a class to match against
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
