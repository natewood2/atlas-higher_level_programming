#!/usr/bin/python3
""" Defines a rectangle module """


class Rectangle():
    """ Defines the rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Attributes for the rectangle """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Makes __width private also the gettor """
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ gettor of the height """
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ Area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter of rectangle """
        if self.width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ print the rectangle with the character #: """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for i in range(self.height):
            rectangle += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """ should return a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ deleting instance of rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest Rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        if area_2 >= area_1:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns new Rectangle
            width == height == size       
        """
        return cls(size, size)