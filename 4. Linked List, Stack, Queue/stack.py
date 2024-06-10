class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    # O(1)
    def push(self, val) -> int:
        node = Node(val)
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            temp = self.first
            self.first = node
            node.next = temp
        self.size += 1
        return self.size

    # O(1)
    def pop(self) -> Node:
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
            print(node.val, end="_")
            node = node.next
        print()


st = Stack()
st.print()
st.push(1)
st.push(2)
st.push(3)
st.print()
st.pop()
st.print()
