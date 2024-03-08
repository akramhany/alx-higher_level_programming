#!/usr/bin/python3
"""
Contains the square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square is a special type of a Rectangle with its width equal its height
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the square info in a certain format.
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __update_val(self, name, value):
        """
        Takes a name of an attribute and set it with a value.
        """

        if name == "id":
            self.id = value
        elif name == "size":
            self.size = value
        elif name == "x":
            self.x = value
        elif name == "y":
            self.y = value

    def update(self, *args, **kwargs):
        """
        Updage the square data with given arguments.
        """

        if len(args) == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    self.__update_val(key, value)
                return

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.size = args[1]

        if len(args) > 2:
            self.x = args[2]

        if len(args) > 3:
            self.y = args[3]
