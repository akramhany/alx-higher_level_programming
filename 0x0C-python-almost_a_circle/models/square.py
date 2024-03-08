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
