#!/usr/bin/python3
"""
The base module in the package.
"""

import json


class Base:
    """
    The base class of all other classes in the project, its goal
    is to manage id attribute in all of the future classes.
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
        returns the json string representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        returns a list from the json string.
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set.
        """

        from models import rectangle
        from models import square

        if cls.get_type() == "Rectangle":
            dummy = rectangle.Rectangle(10, 1)
        else:
            dummy = square.Square(10)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """
        takes a list of objs and save its json string into a file.
        """

        if list_objs is None:
            list_objs = []

        filename = cls.get_type() + ".json"

        json_list = []
        for obj in list_objs:
            json_list.append(obj.to_dictionary())

        json_rep = cls.to_json_string(json_list)

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(json_rep)

    @classmethod
    def get_type(cls):
        return "Base"
