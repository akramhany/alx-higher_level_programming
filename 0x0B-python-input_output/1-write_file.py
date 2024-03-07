#!/usr/bin/python3
"""
Contains a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8) and
    returns the number of characters written.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        written_chars_num = f.write(text)

    return written_chars_num
