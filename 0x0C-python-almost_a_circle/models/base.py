#!/usr/bin/python3
"""
The base module in the package.
"""


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

    def __del__(self):
        if Base.__nb_objects > 0:
            Base.__nb_objects -= 1
