class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    # O(1)
    def push(self, val) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.length += 1

    # O(1)
    def pop(self) -> Node:
        if not self.head:
            return None
        pop_node = self.tail
        node = pop_node.prev
        if node:
            node.next = None
            self.tail = node
        else:
            self.tail = None
            self.head = None

        pop_node.prev = None
        self.length -= 1
        return pop_node

    # O(1)
    def shift(self) -> Node:
        if self.length == 0:
            return None
        curr = self.head.next
        node = self.head

        if curr:
            curr.prev = None
            node.next = None
            self.head = curr
        else:
            self.tail = None
            self.head = None

        self.length -= 1
        return node

    # O(1)
    def unshift(self, val) -> None:
        node = Node(val)
        if self.length == 0:
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
        self.head = node
        self.length += 1

    def print(self) -> None:
        node = self.head
        while node:
            print(node.val, end="->")
            node = node.next
        print(None)

    def closerToLast(self, i) -> bool:
        if self.length == 0:
            return -1
        return (self.length / 2) < i

    # O(n)
    def remove(self, i) -> Node:
        if i == 0:
            return self.shift()
        elif i == self.length - 1:
            return self.pop()
        else:
            node = self.get(i)
            after = node.next
            before = node.prev

            before.next = after
            after.prev = before

            node.prev = None
            node.next = None

            self.length -= 1
            return node

    # O(n)
    def insert(self, val, i) -> None:
        if not self.head:
            return None

        if i == 0:
            self.unshift(val)
        elif i == self.length - 1:
            self.push(val)
        else:
            before = self.get(i - 1)
            after = before.next
            node = Node(val)

            before.next = node
            node.prev = before

            node.next = after
            after.prev = node

            self.length += 1

    # O(n)
    def get(self, i) -> Node:
        if not self.head:
            return None
        if self.closerToLast(i):
            j = self.length - 1
            node = self.tail
            while i != j and node:
                j -= 1
                node = node.prev
        else:
            j = 0
            node = self.head
            while i != j and node:
                j += 1
                node = node.next
        return node

    # O(n)
    def set(self, val, i) -> None:
        node = self.get(i)
        if node:
            node.val = val

    # O(n)
    def reverse(self) -> None:
        if not self.head:
            return None

        p, q, r = None, self.head, self.head
        self.head = self.tail
        self.tail = r
        while r:
            r = r.next

            q.next = p
            if p:
                p.prev = q

            p = q
            q = r


dll = DoublyLinkedList()
dll.push(1)
dll.push(2)
dll.push(3)
dll.push(4)
dll.push(5)
dll.push(6)
dll.print()
print("pop:", dll.pop().val)
dll.print()
print("shift:", dll.shift().val)
dll.print()
print("unshift:", dll.unshift(0))
dll.print()
print("insert at 2:", dll.insert("AA", 2))
dll.print()
print("get 2:", dll.get(2).val)
dll.print()
dll.set("BB", 3)
dll.print()
print("remove 1:", dll.remove(1).val)
dll.print()
dll.reverse()
dll.print()
