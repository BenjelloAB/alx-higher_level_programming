#!/usr/bin/python3
"""Module that defines a Base class"""
import json


class Base:
    """
    A Base class for all the other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        serialize the data into a json string
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Serialize the data into a json string
        and save it in a file
        """
        list_dict = []
        if list_objs is not None:
            for item in list_objs:
                dic_it = item.to_dictionary()
                list_dict.append(dic_it)
            with open("{}.json".format(cls.__name__), "w") as fd:
                json.dump(list_dict, fd)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representationN
        """
        return json.loads(json_string)
