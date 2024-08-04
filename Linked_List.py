"""
This module consists of Linked list data structure with all the methods to implement
"""


class Node:
    """
    To create a node
    """

    def __init__(self, value):
        """
        Takes a value and creates a node
        """
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        prints all the nodes in Linked List
        returns: None
        """
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        appends a node at the end of linked list
        value: value of a node
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        removes the last node from the Linked List
        returns: last node
        """
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """
        adds element at beginning of Linked List
        returns: True
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        removes the first node from the Linked List
        returns: first node
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, index):
        """
        gets the particular index from Linked List
        returns: index node
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """
        sets the particular index value
        index: index of linked list to the value
        value: value to be set
        return: boolean
        """
        temp = self.get(index) #saving for tem
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
        if index<0 or index>self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length-1:
            return self.append(value)
        new_node = Node(value)
        pre = self.get(index-1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        removes the value at given index
        index: where to remove the node
        """

if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.print_list()
    my_linked_list.append(2)
    # my_linked_list.print_list()
    print(my_linked_list.pop())
    my_linked_list.print_list()
