#!/usr/bin/python3
"""
defines class Rectangle
"""


class Rectangle:
    """class representation of a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("the rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("the rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """initializing the rectangle by settin the objet
        with width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for an attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for attribute width"""
        if type(value) is not int:
            raise TypeError("the width must be an integer")
        if value < 0:
            raise ValueError("the width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for an attribute height"""
        if type(value) is not int:
            raise TypeError("the height must be an integer")
        if value < 0:
            raise ValueError("the height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string representation of rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
