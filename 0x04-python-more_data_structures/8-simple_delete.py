#!/usr/bin/python3

def indexOf(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1


def simple_delete(a_dictionary, key=""):
    lst = list(a_dictionary.keys())
    if indexOf(lst, key) != -1:
        del a_dictionary[key]
    return a_dictionary
