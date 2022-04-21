#!/usr/bin/python3
""" Node Class """


class Node():
    """ Definition of a singly-linked list node """
    def __init__(self, data, next_node=None):
        """ Instantiate a node """
        self.data, self.next_node = data, next_node

    @property
    def data(self):
        """ Get the data stored in a node """
        return self.__data

    @data.setter
    def data(self, data):
        """ Set the data stored in a node """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """ Get the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """ Set the next node """
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList():
    """ Definition of a singly-linked list """
    def __init__(self):
        """ Instantiate a singly-linked list """
        self.__head = None

    def __str__(self):
        if self.__head is None:
            return ("")
        tmp = self.__head
        _list = ""
        while tmp is not None:
            _list += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                _list += "\n"
        return (_list)
    def sorted_insert(self, value):
        if self.__head is None or value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        tmp = self.__head
        while tmp.next_node is not None and tmp.next_node.data < value:
            tmp = tmp.next_node
        tmp.next_node = Node(value, tmp.next_node)
