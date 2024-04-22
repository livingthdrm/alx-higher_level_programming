class Node:
    """ A class that defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """ an initialization of the class

        attributes:
        data - private instance """
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        """ a property to retrieve the data """
        return self.__data

    @data.setter
    def data(self, value):
        """ a setter for the data value
        if data is not an integer, raise a TypeError exception """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """ a method to retrieve next_node object """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ a method to set the next_node object """
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """ A class that defines a singly linked based on Node """
    def __init__(self):
        """ An initialization of class singly linked list """
        self.__head = None

    def __iter__(self):
        """ making the node iterable """

        node = self.__head
        while node:
            yield node.__data
            node = node.next_node

    def __repr__(self):
        """ iterate to get all the data """
        return " ".join(map(repr, self))

    def sorted_insert(self, value):
        """ A method to insert a new node """
        new_node = Node(value)
        prev = None
        node = self.__head
        while node and node.__data < value:
            prev = node
            node = node.__next_node
            if prev:
                prev.next_node = new_node
            else:
                self.__head = new_node
            new_node.next_node = node
