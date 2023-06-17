#!/usr/bin/python3
""" Defines the Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represents a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a square instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieves the size """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

