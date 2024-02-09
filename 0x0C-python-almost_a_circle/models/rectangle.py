#!/usr/bin/python3
"""
   Contains the Rectangle class which inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
        Represents a rectangle, inheriting from Base.

        Attributes:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the rectangle's position.
            y: The y-coordinate of the rectangle's position.
            id: The unique identifier of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
           Initializes a Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Getter function for width.

            Returns: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter function for width.

            Args:
                value (int): The width value to be set.

            Raises:
                  TypeError: If the value is not an integer.
                  ValueError: If the value is not positive.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            Getter function for height.

            Returns: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter function for height.

            Args:
                value (int): The height value to be set.

            Raises:
                  TypeError: If the value is not an integer.
                  ValueError: If the value is not positive.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            Getter function for x.

            Returns: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setter function for x.

            Args:
                value (int): The x-coordinate value to be set.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is negative.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            Getter function for y.

            Returns: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setter function for y.

            Args:
                value (int): value to be set.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is negative.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Displays the rectangle as a series of '#' characters.
        """
        rectangle = ""
        print_symbol = "#"

#        for i in range(self.__height - 1):
#            rectangle += print_symbol * self.__width + "\n"
#        rectangle += print_symbol * self.__width

#        print("{}".format(rectangle))

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """
           Returns the string representation of the rectangle.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Variable number of non-keyword arguments.
            **kwargs: Variable number of keyword arguments.
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
           Returns the dictionary representation of the rectangle.
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
