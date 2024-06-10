class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertex(self, node: str) -> None:
        if not self.adjacency_list.get(node):
            self.adjacency_list[node] = []

    def add_edge(self, node_1: str, node_2: str) -> None:
        if (
            self.adjacency_list[node_1] is not None
            and self.adjacency_list[node_2] is not None
        ):
            self.adjacency_list[node_1].append(node_2)
            self.adjacency_list[node_2].append(node_1)

    def remove_edge(self, node_1, node_2) -> None:
        if (
            node_2 in self.adjacency_list[node_1]
            and node_1 in self.adjacency_list[node_2]
        ):
            self.adjacency_list[node_1].remove(node_2)
            self.adjacency_list[node_2].remove(node_1)

    def remove_vertex(self, node) -> None:
        if self.adjacency_list[node]:
            for i in self.adjacency_list[node]:
                self.remove_edge(i, node)
            del self.adjacency_list[node]

    def dfs_recursive(self, node) -> None:
        node_list, visited = [], {}

        adjacency_list = self.adjacency_list

        def dfs(vertex) -> None:
            if not vertex:
                return None
            visited[vertex] = True
            node_list.append(vertex)

            for i in adjacency_list[vertex]:
                if not visited.get(i):
                    return dfs(i)

        dfs(node)

        print(node_list)

    def dfs_iterative(self, node) -> None:
        node_list, visited, stack = [], {}, [node]
        visited[node] = True

        while len(stack) != 0:
            cur_node = stack.pop()
            node_list.append(cur_node)

            for i in self.adjacency_list[cur_node]:
                if not visited.get(i):
                    visited[i] = True
                    stack.append(i)

        print(node_list)

    def bfs_iterative(self, node) -> None:
        node_list, visited, queue = [], {}, [node]
        visited[node] = True

        while len(queue) != 0:
            cur_node = queue.pop(0)
            node_list.append(cur_node)

            for i in self.adjacency_list[cur_node]:
                if not visited.get(i):
                    visited[i] = True
                    queue.append(i)

        print(node_list)


graph = Graph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")

graph.add_edge("a", "b")
graph.add_edge("c", "b")
graph.add_edge("a", "c")

# {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'a']}

graph.remove_edge("a", "c")

# {'a': ['b'], 'b': ['a', 'c'], 'c': ['b']}

graph.remove_vertex("a")

# {'b': ['c'], 'c': ['b']}

graph.add_vertex("a")
graph.add_vertex("d")
graph.add_vertex("e")
graph.add_vertex("f")
graph.add_edge("a", "c")
graph.add_edge("b", "d")
graph.add_edge("e", "c")
graph.add_edge("d", "e")
graph.add_edge("d", "f")
graph.add_edge("e", "f")

graph.dfs_recursive("a")

# ['a', 'c', 'b', 'd', 'e', 'f']

graph.dfs_iterative("a")

# ['a', 'c', 'e', 'f', 'd', 'b']

graph.bfs_iterative("a")

# ['a', 'c', 'b', 'e', 'd', 'f']
