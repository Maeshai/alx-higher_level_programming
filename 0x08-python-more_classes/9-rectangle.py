 class Rectangle
"""


class Rectangle:
    """
        Initialze the rectangle class with width and
        height fields
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        # self.print_symbol = '#'

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
                my_print += str(self.print_symbol)
            if i < self.__height - 1:
                my_print += '\n'
        return my_print

    def __repr__(self):
        """
            Modify the special method __repr__
        """
        return "Rectangle(" + str(self.__width) + ', ' + str(self.__height)+')'

    def __del__(self):
        """
            Modify the special method __del__
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            method to return the bigger of 2 rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
