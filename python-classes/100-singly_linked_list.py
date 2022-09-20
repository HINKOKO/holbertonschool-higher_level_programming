#!/usr/bin/python3
"""Module 7"""

"""class Node defines a node of singly-linked list"""


class Node:
    """Instantiation with data and next_node"""

    def __init__(self, data, next_node=None):
        """Initializes Node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter - to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter - to set value to data"""
        if value is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter - to retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter - to set value to  next_node"""
        if type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Instantiation with __init__"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        """String printer"""
        printer = ""
        current = self.__head
        while current:
            printer += str(current.data)
            current = current.next_node
            printer += "\n"
            return printer

    def sorted_insert(self, value):
        """
        Inserts new node according to increasing order
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        elif self.__head.data > new.data:
            self.__head = new
            return
        else:
            tmp = self.__head
            while new.data > tmp.data and tmp.next_node is not None:
                tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new
                return
