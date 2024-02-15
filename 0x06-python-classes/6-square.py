#!/usr/bin/python3
"""A module that contains the Square Class."""


class Square:
    """A class that represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        position = self.position
        if (size == 0):
            print()
        else:
            for i in range(position[1]):
                print()
            for i in range(size):
                for j in range(size + position[0]):
                    if j < position[0]:
                        print(' ', end='')
                    else:
                        print('#', end='')
                print()
