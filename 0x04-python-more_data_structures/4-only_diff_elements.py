#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set1 = set_1.difference(set_2)
    set2 = set_2.difference(set_1)
    return set1.union(set2)
