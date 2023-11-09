#!/usr/bin/python3

def max_items(items):
    maxy = items[0][1]
    for i in range(1, len(items)):
        if maxy < items[i][1]:
            maxy = items[i][1]
            name = items[i][0]
    return name


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    items = list(a_dictionary.items())
    info_tuple = max_items(items)
    return info_tuple
