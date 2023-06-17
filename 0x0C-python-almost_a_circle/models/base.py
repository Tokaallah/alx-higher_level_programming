#!/usr/bin/python3

"""
This module contains the Base class.
"""

class Base:
    """
    Base class for managing id attribute in all other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base instance.
        If id is provided, assign it to the public instance attribute 'id'.
        Otherwise, increment __nb_objects and assign the new value to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects