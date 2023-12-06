#!/usr/bin/python3
''' a Module that defines a class Student '''


class Student:
    '''Class of the student'''

    def __init__(self, first_name, last_name, age):
        '''__init__ function'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' to_json function
        '''
        return self.__dict__
