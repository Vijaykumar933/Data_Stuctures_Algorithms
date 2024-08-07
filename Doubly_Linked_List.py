"""
This module consists of Doubly Linked list data structure with all the methods to implement
"""


class Node:
    """
    To create a node
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Create a Data structure DoublyLinkedList
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        prints all the nodes in DoublyLinkedList
        returns: None
        """
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        appends a node at the end of DoublyLinkedList
        value: value of a node
        """
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        removes the last node from the DoublyLinkedList
        returns: last node
        """
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        """
        adds element at beginning of DoublyLinkedList
        returns: True
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        removes the first node from the DoublyLinkedList
        returns: first node
        """
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """
        gets the particular index from DoublyLinkedList
        index: index value to be returned
        returns: index node
        """
        if index < 0 or index >= self.length:
            return None

        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        """
        sets the particular index value
        index: index of DoublyLinkedList to the value
        value: value to be set
        return: boolean
        """
        temp = self.get(value)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        inserts new node at the given index
        index: to insert the node
        value : node value
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)

        temp.next.prev = new_node
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp

        self.length += 1
        return True


    def remove(self, index):
        """
        removes the value at given index
        index: where to remove the node
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.print_list()
    my_doubly_linked_list.append(2)
    # my_doubly_linked_list.print_list()
    print(my_doubly_linked_list.pop())
    my_doubly_linked_list.print_list()