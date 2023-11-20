#!/usr/bin/python3

def indexOf(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1


def uniq_add(my_list=[]):
    new_lst = []
    for i in range(len(my_list)):
        if indexOf(new_lst, my_list[i]) == -1:
            new_lst.append(my_list[i])
    s = 0
    for i in range(len(new_lst)):
        s += new_lst[i]
    return s
