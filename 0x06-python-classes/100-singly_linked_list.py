#!/usr/bin/python3
"""This module contains the implementation of the Node class
    and the SinglyLinkedList class"""


class Node:
    """the Node class contains a variable to store the data
        a pointer to the next node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __getattr__(self, name):
        return self.__dict__["__{}".format(name)]

    def __setattr__(self, name, value):
        if name == 'data':
            if not isinstance(value, int):
                raise TypeError('data must be an integer')

        elif name == 'next_node':
            if value is not None and not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")

        self.__dict__["__{}".format(name)] = value


class SinglyLinkedList:
    """This class represents the singly linked list data structure
        using Node class as the nodes"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        else:
            ptr = self.__head
            if ptr.data > value:
                new_node.next_node = self.__head
                self.__head = new_node
                return

            while ptr.next_node is not None and ptr.next_node.data <= value:
                ptr = ptr.next_node

            new_node.next_node = ptr.next_node
            ptr.next_node = new_node

    def __str__(self):
        ptr = self.__head
        str_list = ""
        while ptr is not None:
            data = "{}".format(ptr.data)
            if ptr.next_node is not None:
                data += "\n"

            str_list += data
            ptr = ptr.next_node

        return str_list
