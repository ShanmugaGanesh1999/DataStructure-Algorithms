class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # O(log n)
    def insert(self, val) -> int:
        if not self.root:
            self.root = Node(val)
            return val
        node = self.root
        while True:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(val)
                    return val
            elif node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(val)
                    return val
            else:
                return -1

    # O(log n)
    def search(self, x) -> Node:
        if not self.root:
            return None
        node = self.root
        found = False
        while node and not found:
            if node.val == x:
                found = True
            elif node.val > x:
                node = node.left
            elif node.val < x:
                node = node.right
        return node if found else None

    # O(v+e)
    def bfs(self) -> list:
        visited, queue = [], []
        if not self.root:
            return None
        node = self.root
        queue.append(node)
        while len(queue) != 0:
            node = queue.pop(0)  # popping the 0th index element
            visited.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return visited

    # O(v+e)
    def dfs_pre_order(self) -> list:
        if not self.root:
            return None
        visited = []

        def pre_order(node: Node) -> None:
            if node:
                visited.append(node.val)
                pre_order(node.left)
                pre_order(node.right)

        pre_order(self.root)
        return visited

    # O(v+e)
    def dfs_post_order(self) -> list:
        if not self.root:
            return None
        visited = []

        def post_order(node: Node) -> None:
            if node:
                post_order(node.left)
                post_order(node.right)
                visited.append(node.val)

        post_order(self.root)
        return visited

    # O(v+e)
    def dfs_in_order(self) -> list:
        if not self.root:
            return None
        visited = []

        def in_order(node: Node) -> None:
            if node:
                in_order(node.left)
                visited.append(node.val)
                in_order(node.right)

        in_order(self.root)
        return visited


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(8)
bst.insert(4)
print("search 4:", bst.search(4))
print("search 2:", bst.search(2))
bst.insert(1)
print("search 1:", bst.search(1))
print("bfs:", bst.bfs())
print("dfs_pre", bst.dfs_pre_order())
print("dfs_in", bst.dfs_in_order())
print("dfs_post", bst.dfs_post_order())

"""
    5
  3   7
1  4 6  8
"""
