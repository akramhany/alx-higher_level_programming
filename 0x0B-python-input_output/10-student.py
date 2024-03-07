#!/usr/bin/python3
"""
Contains Student class.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dt = self.__dict__

        if attrs is None:
            return dt

        new_dt = {}
        for attr in attrs:
            if attr in dt:
                new_dt[attr] = dt[attr]

        return new_dt
