#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for key in new_dict:
        mul = new_dict[key] * 2
        new_dict[key] = mul
    return new_dict
