#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """A class that represents a square.

    Attributes:
        __size: The length of a side of the square.
        __position: The position of the square.

    Methods:
        __init__: Initializes a new instance of the Square class.
        __str__: Returns a string representation of the square.
        size: Getter method to retrieve the size of the square.
        size: Setter method to set the size of the square.
        position: Getter method to retrieve the position of the square.
        position: Setter method to set the position of the square.
        area: Calculates the area of the square.
        pos_print: Returns the position of the square in spaces.
        my_print: Prints the square in position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size: Length of a side of Square.
            position: Coordinates where the square is located.
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """The property of size as the length of a side of Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """The property of the coordinates of this Square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of this Square.

        Args:
            value: A tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple or any int in tuple < 0.
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate the area of the square..

        Returns:
            int: The square of the size.
        """
        return self.__size * self.__size

    def pos_print(self):
        """Returns the position in spaces."""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Print the square in position."""
        print(self.pos_print(), end='')
