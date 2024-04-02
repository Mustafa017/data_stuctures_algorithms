"""
# Linked List Practice

Implement a linked list class. Your class should be able to:

+ Append data to the tail of the list and prepend to the head
+ Search the linked list for a value and return the node
+ Remove a node
+ Pop, which means to return the first node's value and delete the node from the list
+ Insert data at some position in the list
+ Return the size (length) of the linked list

"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def to_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next
        return out_list

    def search(self, value):
        pass

    def pop(self):
        if self.head:
            res = self.head.value
            del self.head.value
        return res

    def __len__(self):
        return len(self.to_list())


if __name__ == "__main__":
    d = LinkedList()
    d.append(6)
    d.append(2)
    d.append(1)
    print(d.head.value)
    print(d.to_list())
    print(d.__len__())
    print(d.pop())
    print(d.to_list())


# 3141592653589793238462643383279
# ['314', '14', '15926535897', '9323', '4', '8462643383279']
