#!/usr/bin/python3

"""
Rectangle Class Module that inherits from Base:

Init Superclass' `id` (Base)
Private instance attributes, each with its own public getter and setter:
__width -> width, __height -> height, __x -> x, __y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Contain public methods of area and display:
def area(self): that returns the area value of the Rectangle instance
def display(self): prints Rectangle instance to stdout with the `#` character
:- improve display method to take care of x and y.
Update Rectangle class by overriding the __str__ method
so that it returns "[Rectangle] (<id>) <x>/<y> - <width>/<height>"
Contain public method: def update(self, *args, **kwargs):
that assigns a key/value argument to attributes: if *args,
set attrs in this order arg1=id, arg2=width, arg3=height, arg4=x, arg5=y
if no args given, set according to kwargs.
Add public method def to_dictionary(self):
that returns the dictionary representation of a Rectangle.
"""


from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an interger")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an interger")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for g in range(self.y):
            print()
        for g in range(0, self.height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """Return string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):

        """Update Rectangle attributes"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
