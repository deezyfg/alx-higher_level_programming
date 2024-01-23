#!/usr/bin/python3
"""Module for a singly linked list."""


class Node:
    """Defines a node.

    Attributes:
        __data: The data of the node.
        __next_node: The next node in the linked list.

    Methods:
        __init__: Initializes a new instance of the Node class.
        data: Getter method to retrieve the data of the node.
        data: Setter method to set the data of the node.
        next_node: Getter method to retrieve the next node in the list.
        next_node: Setter method to set the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """initializes the node with instance variables."""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets data attribute."""

        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data attribute."""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Gets next_node attribute.

        Returns: next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets value of next node."""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list.

    Attributes:
        head: The head of the linked list.

    Methods:
        __init__: Initializes a new instance of the SinglyLinkedList class.
        __str__: String representation of the linked list.
        sorted_insert: Inserts a node in a sorted fashion.
    """

    def __init__(self):
        """Initializes the singly linked list"""

        self.head = None

    def __str__(self):
        """Make list printable"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """Insert in a sorted fashion.

        Args:
            value: The value to be on the node.
        """

        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
