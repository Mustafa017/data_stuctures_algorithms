class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def to_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next
        return out_list


if __name__ == "__main__":
    d = LinkedList()
    d.append(5)
    d.append(0)
    d.append(7)
    d.append(3)
    d.append(9)
    print(d.to_list())
