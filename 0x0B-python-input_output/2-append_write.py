#!/usr/bin/python3
"""
Contains a function that appends a string to a text file
"""


def append_write(filename="", text=""):
    """
    a function that appends a string to a text file (UTF8) and
    returns the number of characters written.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        written_chars_num = f.write(text)

    return written_chars_num
