#!/usr/bin/python3

def max_lst(lst):
    maxy = lst[0]
    for i in range(1, len(lst)):
        if maxy < lst[i]:
            maxy = lst[i]
            index = i
    return (maxy, index)


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    lst_vals = list(a_dictionary.values())
    lst_keys = list(a_dictionary.keys())
    info_tuple = max_lst(lst_vals)
    return lst_keys[info_tuple[1]]    
