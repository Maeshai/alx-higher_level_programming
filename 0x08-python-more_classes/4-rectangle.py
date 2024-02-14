#!/usr/bin/python3
"""
    define a class Rectangle
"""


class Rectangle:
    """
        Initialze the rectangle class with width and
        height fields
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Get the value of the width field
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Set the value of the width field
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Get the value of the height field
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Set the value of the height field
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Get the area width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Get the perimeter width(2) + height(2)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
            Modify the special method __str__
        """
        my_print = ""
        if self.__height == 0 or self.__width == 0:
            return my_print
        for i in range(self.__height):
            for j in range(self.__width):
                my_print += '#'
            if i < self.__height - 1:
                my_print += '\n'
        return my_print

    def __repr__(self):
        """
            Modify the special method __repr__
        """
        return "Rectangle(" + str(self.__width) + ', ' + str(self.__height)+')'
