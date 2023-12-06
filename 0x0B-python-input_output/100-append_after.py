#!/usr/bin/python3
"""
function that searches and updates
"""


def append_after(filename="", search_string="", new_string=""):
    '''function to insert a line after a string

    Args:
       filename (str):  name of the file
       search_string (str): string to search for
       new_string (str):  string to insert
    '''
    txt = ""
    with open(filename) as myfile_r:
        for line in myfile_r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as myfile_w:
        myfile_w.write(txt)
