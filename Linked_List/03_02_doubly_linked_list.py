class DoubleNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


if __name__ == "__main__":
    d = DoubleLinkedList()
    d.append(6)
    d.append(9)
    d.append(2)
    d.append(1)
    print(d.head.value)  # 6
    print(d.tail.value)  # 1
    print(d.head.next.value)  # 9
    print(d.head.next.next.value)  # 2
    print(d.head.next.next.previous.value)  # 9
    print(d.tail.next.value)  # AttributeError
