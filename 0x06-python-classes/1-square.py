#!/usr/bin/python3

"""Module defining a Square class."""


class Square:
    """A class that represents a square.

    Attributes:
        __size: The size of the square.

    Methods:
        __init__: Initializes a new instance of the Square class.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the new square.
        """
        self.__size = size
