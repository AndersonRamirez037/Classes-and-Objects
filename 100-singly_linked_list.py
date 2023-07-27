#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value, None)
        if self.__head is None:
            self.__head = new_node
        else:
            if value <= self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                current = self.__head
                while current.next_node is not None and current.next_node.data < value:
                    current = current.next_node
                new_node.next_node = current.next_node
                current.next_node = new_node

    def __str__(self):
        if not self.__head:
            return ''
        else:
            current = self.__head
            elements = []
            while current is not None:
                elements.append(str(current.data))
                current = current.next_node
            return '\n'.join(elements)