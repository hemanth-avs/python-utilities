"""
    Linked List
"""


class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

    def __repr__(self):
        if self.data:
            return str(self.data)
        else:
            return ""


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def get_size(self):
        return self._size

    def __len__(self):
        return self._size

    def append(self, data):
        """
        Element will be append to tail of the LinkedList
        :param data: Element
        :return: Node
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

        self._size = self._size + 1
        return new_node

    def appendleft(self, data):
        """
        Element will append to left of List as Head
        :param data: Element
        :return: Node
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size = self._size + 1
        return new_node

    def append_after(self, prev_node_data, data):
        """
        Element will be added Next of Previous Node provided
        :param prev_node_data: Node
        :param data: Element
        :return: New Node
        """
        new_node = Node(data)
        new_node.next = prev_node_data.next
        prev_node_data.next = new_node
        self._size = self._size + 1
        return new_node

    def __repr__(self):
        """
        String Representation of Linked List
        :return: String
        """
        node = self.head
        return_str = ""
        while node:
            return_str = return_str + str(node) + " -> "
            node = node.next
        return return_str[:-4]
