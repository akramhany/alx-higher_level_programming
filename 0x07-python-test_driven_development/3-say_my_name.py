#!/usr/bin/python3

""" contains say_my_name function """


def say_my_name(first_name, last_name=""):
    """
    takes the first name and the last name and prints a message
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
