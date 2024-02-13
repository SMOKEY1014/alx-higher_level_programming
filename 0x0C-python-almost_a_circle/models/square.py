#!/usr/bin/python3

"""
Square Class Module that inherits from Rectangle:
Inits superclass' id, width (as size), height (as size), x, y
Class constructor: __init__(self, size, x=0, y=0, id=None)
Contains public attribute size
Contain public method of:
update(*args, **kwargs)
to_dictionary(self)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        return "[Square] ({}) {}/{} - {}".format(id, x, y, width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):

        """Update Rectangle attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
