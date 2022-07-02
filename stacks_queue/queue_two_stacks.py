import queue
import sys


class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enque(self, item):
        self.s1.insert(0, item)

    def deque(self):
        self.s2.append(self.s1.pop())

    def peek(self):
        return self.s1[-1]

    def __str__(self) -> str:
        return self.s1, self.s2


myQueue = Queue()
t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        myQueue.enque(arr[1])
    elif arr[0] == 2:
        myQueue.deque()
    else:
        print(myQueue.peek())

# sample input
# 10
# 1 42
# 2
# 1 14
# 3
# 1 28
# 3
# 1 60
# 1 78
# 2
# 2

# sample output
# 14
# 14
