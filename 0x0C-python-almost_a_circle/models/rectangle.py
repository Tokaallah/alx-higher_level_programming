#!/usr/bin/python3
""" Defines the Rectangle class """

from models.base import Base

class Rectangle(Base):
    """ Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Returns the area of the Rectangle instance """
        return self.width * self.height

    def display(self):
        """ Prints the Rectangle instance with '#' characters """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ Returns a string representation of the Rectangle instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """ Updates the attributes of the Rectangle instance """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """ Returns a dictionary representation of the Rectangle instance """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

