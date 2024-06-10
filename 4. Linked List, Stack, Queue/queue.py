class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    # O(1)
    def enqueue(self, val) -> None:
        node = Node(val)
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    # O(1)
    def dequeue(self) -> Node:
        if self.size == 0:
            return None
        node = self.first

        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.size -= 1
        return node

    def print(self) -> None:
        node = self.first
        while node:
            print(node.val, end="<-")
            node = node.next
        print()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print()
q.dequeue()
q.print()
