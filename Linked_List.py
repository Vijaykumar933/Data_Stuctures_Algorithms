"""
This module consists of Linked list data structure with all the methods to implement
"""
class Node:
    """To create a node"""
    def __init__(self,value):
        """Takes a value and creates a node"""
        self.value = value
        self.next = None

class Linked_List:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1



if __name__ =="__main__":
    my_linked_list = Linked_List(1)
    my_linked_list.print_list()
    my_linked_list.append(2)
    my_linked_list.print_list()

    


