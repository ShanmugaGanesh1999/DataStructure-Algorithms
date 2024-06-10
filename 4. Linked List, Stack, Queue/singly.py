class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    # O(1)
    def push(self, val) -> Node:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1
        return self.tail

    # O(1)
    def pop(self) -> Node:
        if not self.head:
            return None
        pre = self.head

        while pre.next != None:
            pre = pre.next

        pop_node = pre
        pre.next = None
        self.length -= 1

        if self.length != 0:
            self.tail = pre
        else:
            self.head = None
            self.tail = None
        return pop_node

    # O(1)
    def shift(self) -> Node:
        if not self.head:
            return None

        node = self.head
        node = node.next
        self.length -= 1
        self.head = node

        return self.head

    # O(1)
    def unshift(self, val) -> Node:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1
        return self.head

    def print(self) -> None:
        node = self.head

        while node:
            print(node.val, end="->")
            node = node.next
        print(None)

    # O(n)
    def get(self, i) -> Node:
        if not self.head or i < 0 or i > self.length:
            return None
        node = self.head
        j = 0
        while j != i:
            node = node.next
            j += 1
        return node

    # O(n)
    def set(self, val, i) -> None:
        node = self.get(i)
        if node:
            node.val = val
            return True
        return False

    # O(n)
    def insert(self, val, i) -> None:
        if i == 0:
            self.unshift(val)
        elif i == self.length - 1:
            self.push(val)
        else:
            pre = self.get(i - 1)
            node = Node(val)
            node.next = pre.next
            pre.next = node
            self.length += 1

    # O(n)
    def remove(self, i) -> Node:
        if i == 0:
            return self.shift()
        elif i == self.length - 1:
            return self.pop()
        else:
            node = self.get(i - 1)
            removed = node.next
            node.next = removed.next
            self.length -= 1
            return removed

    # O(n)
    def search(self, n) -> int:
        if not self.head:
            return -1
        node = self.head
        i = 0
        while node and node.val != n:
            node = node.next
            i += 1
        return i if node.val == n else -1

    # O(n)
    def reverse(self) -> None:
        if not self.head:
            return None
        node = self.head
        pre = None
        next = self.head

        self.head = self.tail
        self.tail = node
        while next:
            next = node.next
            node.next = pre

            pre = node
            node = next


ssl = SinglyLinkedList()
ssl.push(1)
ssl.print()
print(ssl.pop().val)
ssl.print()
ssl.push(2)
ssl.push(3)
ssl.push(4)
ssl.push(5)
ssl.print()
print(ssl.shift().val)
ssl.print()
print(ssl.unshift(1).val)
ssl.print()
print("get3index", ssl.get(3).val)
ssl.print()
print("set0toAA", ssl.set("AA", 0))
ssl.print()
print("set0toAA", ssl.set("BB", 7))
ssl.print()
print("insert2", ssl.insert("BB", 2))
ssl.print()
print("remove3", ssl.remove(3).val)
ssl.print()
print("reserve", ssl.reverse())
ssl.print()
print("searchIndex", ssl.search("AA"))
