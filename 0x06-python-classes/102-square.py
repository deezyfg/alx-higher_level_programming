#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """A class that represents a square.

    Attributes:
         __size: Length of a side of the square.

    Methods:
        __init__: Initializes a new instance of the Square class.
        size: Getter method to retrieve the size of the square.
        size: Setter method to set the size of the square.
        area: Calculates the area of the square.
        __le__: Less than or equal to comparison for squares.
        __lt__: Less than comparison for squares.
        __ge__: Greater than or equal to comparison for squares.
        __ne__: Not equal to comparison for squares.
        __gt__: Greater than comparison for squares.
        __eq__: Equal to comparison for squares.
    """

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size: Length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Property of the length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

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
        """Calculate the area of the square.

        Returns:
            int: The square of the size.
        """
        return self.__size * self.__size

    def __le__(self, other):
        """Less than or equal to comparison for squares."""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Less than comparison for squares."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison for squares."""
        return self.area() >= other.area()

    def __ne__(self, other):
        """Not equal to comparison for squares."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison for squares."""
        return self.area() > other.area()

    def __eq__(self, other):
        """Equal to comparison for squares."""
        return self.area() == other.area()
