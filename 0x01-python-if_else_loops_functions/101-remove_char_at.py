#!/usr/bin/python3
def remove_char_at(str, n):
    str_tr = ""
    for i, char in enumerate(str):
        if i != n:
            str_tr += char
    return str_tr
