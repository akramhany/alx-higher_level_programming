#!/usr/bin/python3
"""
Contains a function that would read and print the content of a given file name.
"""


def read_file(filename=""):
    """
    a function that reads and print the content of a file.
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
