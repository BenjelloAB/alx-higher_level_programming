#!/usr/bin/python3
''' module that defines a function that
 returns the list of methods of an obj'''


def lookup(obj):
    ''' function that returns a list methods in an obj
    '''
    return dir(obj)
