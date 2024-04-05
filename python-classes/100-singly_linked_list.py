#!/usr/bin/python3
"""Define a class for Node (a node of a singly linked list)"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        # Node data and pointer to the next node

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        # Getter for node data
        return self.__data

    @data.setter
    def data(self, value):
        # Setter for node data --> ensures it's an integer

        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        # Getter for the next node
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        # Setter for the next node --> ensures it's a Node object

        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    # Constructor to initialize the linked list

    def __init__(self):
        # Head of the list
        self.head = None

    def __str__(self):
        # String representation of the list

        ret = ""
        node = self.head

        while node:
            ret += str(node.data) + "\n"  # Append node data to string
            node = node.next_node

        return ret[:-1]  # Return all but the last newline

    def sorted_insert(self, value):
        # Insert a new node with the given value in sorted order

        new = Node(value)

        if not self.head:
            # If list is empty, new node becomes head
            self.head = new
            return

        if value < self.head.data:
            # Insert new node before head for ascending order
            new.next_node = self.head
            self.head = new
            return

        # Traverse list to find the correct position for new node
        node = self.head

        while node.next_node and node.next_node.data < value:
            node = node.next_node

        if node.next_node:
            # Insert new node in its sorted position
            new.next_node = node.next_node
        node.next_node = new
