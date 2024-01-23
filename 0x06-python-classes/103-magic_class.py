#!/usr/bin/python3
"""Magic class from a given ByteCode."""
import math


class MagicClass:
    """Set up the magic.

    Attributes:
        __radius: The radius of the magic.

    Methods:
        __init__: Initializes a new instance of the MagicClass.
        area: Calculates the area of the magic.
        circumference: Calculates the circumference of the magic.
    """

    def __init__(self, radius=0):
        """Magic class constructor.

        Args:
            radius: The radius of the magic.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculation of the area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculation of the circumference."""
        return 2 * math.pi * self.__radius
