#!/usr/bin/python3
"""Module that defines a Base class"""
import json


class Base:
    """
    A Base class for all the other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize the instance
        """
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
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
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
                json_d = json.loads(cls.to_json_string(dic_it))
                list_dict.append(json_d)
        with open("{}.json".format(cls.__name__), "w") as fd:
            json.dump(list_dict, fd)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representationN
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Creates an instance with all the attributes ready set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r = Rectangle(4, 7)
        if cls.__name__ == "Square":
            r = Square(7)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """
            a method that returns a list of instances from a file
        """
        file_name = cls.__name__ + ".json"
        instances = []
        try:
            with open(file_name, "r") as fd:
                json_data = fd.read()
                data = cls.from_json_string(json_data)
        except FileNotFoundError:
            return instances

        for item in data:
            r = cls.create(**item)
            instances.append(r)

        return instances
