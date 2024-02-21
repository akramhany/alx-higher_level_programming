#!/usr/bin/python3

""" A module that contain the rectangle class (ALX task 0) """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        return self.__represent_with_symbol()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __represent_with_symbol(self):
        result = ""

        if self.width == 0 or self.height == 0:
            return result

        symbol = str(type(self).print_symbol)

        if hasattr(self, 'print_symbol'):
            symbol = str(self.print_symbol)

        for i in range(self.height):
            for j in range(self.width):
                result += symbol

            if i != self.height - 1:
                result += "\n"

        return result
