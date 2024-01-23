#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """A class that represents a square.

    Attributes:
        __size: The size of the square.

    Methods:
        __init__: Initializes a new instance of the Square class.
        size: Getter method to retrieve the size of the square.
        size: Setter method to set the size of the square.
        area: Calculates the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square.

        Returns:
            int: The square of the size.
        """
        return (self.__size ** 2)
