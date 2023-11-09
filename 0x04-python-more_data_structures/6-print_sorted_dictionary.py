#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    lst = a_dictionary.keys()
    lst = sorted(lst, reverse=False)
    for i in range(len(lst)):
        print("{}: {}".format(lst[i], a_dictionary[lst[i]]))
