#!/usr/bin/python3
"""
Contains the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    A shape class of the base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        # assign attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Returns the area of the rectangle by multiplying width by height.
        """

        return self.width * self.height

    def display(self):
        """
        Represents and display the rectangle as #, while taking care x and y
        """

        for i in range(self.y):
            print()

        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """
        Returns the rectangle info in a certain format.
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def __update_val(self, name, value):
        """
        Takes a name of an attribute and set it with a value.
        """

        if name == "id":
            self.id = value
        elif name == "width":
            self.width = value
        elif name == "height":
            self.height = value
        elif name == "x":
            self.x = value
        elif name == "y":
            self.y = value

    def update(self, *args, **kwargs):
        """
        Updage the rectangle data with given arguments.
        """

        if len(args) == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    self.__update_val(key, value)
                return

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.width = args[1]

        if len(args) > 2:
            self.height = args[2]

        if len(args) > 3:
            self.x = args[3]

        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """

        return self.__dict__()

    def __dict__(self):

        dt = {}
        dt["id"] = self.id
        dt["width"] = self.width
        dt["height"] = self.height
        dt["x"] = self.x
        dt["y"] = self.y
        return dt

    @classmethod
    def get_type(cls):
        return "Rectangle"
