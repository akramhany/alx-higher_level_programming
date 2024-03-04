#!/usr/bin/python3
"""
the first advanced task
"""


class MyInt(int):
    """
    a Rebel class that has its == and != inverted.
    """

    def __eq__(self, num):
        return int(self) != int(num)

    def __ne__(self, num):
        return int(self) == int(num)
