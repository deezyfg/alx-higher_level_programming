#!/usr/bin/python3
"""Defines a Square subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a subclass of Rectangle."""

    def __init__(self, size):
        """Initializes a new Square with a given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
