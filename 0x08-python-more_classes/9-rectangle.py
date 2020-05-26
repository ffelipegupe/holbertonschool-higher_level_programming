#!/usr/bin/python3
"""Rectangle Class source"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """width value setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Public instance method that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """String method"""
        if self.__width == 0 or self.__height == 0:
            return ""
        lenght = str(self.print_symbol) * self.__width
        return (lenght + "\n") * (self.__height - 1) + lenght

    def __repr__(self):
        """String representation of a rectangle using eval()"""
        str_w = str(self.__width)
        str_h = str(self.__height)
        return "Rectangle(" + str_w + ", " + str_h + ")"

    def __del__(self):
        """del method"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new Rectangle"""
        cls.number_of_instances += 1
        return cls(size, size)
