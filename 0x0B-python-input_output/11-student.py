#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """Class that modelize a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.with a list
        constraint
        Args:
            attrs (list):A list of the attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Function to replace all attributes of a student obj
        Args:
            json (dict): key/value pairs to replace attributes with
        """
        for k, v in json.items():
            setattr(self, k, v)
