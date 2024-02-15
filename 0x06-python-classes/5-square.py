#!/usr/bin/python3
"""A module that contains the Square Class."""


class Square:
    """A class that represents a square."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        size = self.size
        if (size == 0):
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print('#', end='')
                print()
