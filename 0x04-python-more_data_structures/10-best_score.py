#!/usr/bin/python3

def max_items(items):
    max_name, max_score = items[0]
    for name, score in items:
        if max_score < score:
            max_score = score
            max_name = name
    return max_name


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    items = list(a_dictionary.items())
    if not items:
        return None
    info_tuple = max_items(items)
    return info_tuple
