from queue import PriorityQueue


class Dijkstra:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertex(self, node: str) -> None:
        if not self.adjacency_list.get(node):
            self.adjacency_list[node] = []

    def add_edge(self, node_1: str, node_2: str, weight: int) -> None:
        if (
            self.adjacency_list[node_1] is not None
            and self.adjacency_list[node_2] is not None
        ):
            self.adjacency_list[node_1].append((node_2, weight))
            self.adjacency_list[node_2].append((node_1, weight))

    def dijkstra_algo(self, start, end) -> list:
        queue = PriorityQueue()
        previous, distance = {}, {}
        # initiallizing the variables
        for i in self.adjacency_list:
            if i == start:
                distance[i] = 0
                queue.put((0, i))
            else:
                distance[i] = float("inf")
                queue.put((float("inf"), i))
            previous[i] = None

        smallest, path = None, []
        while queue.qsize():  # run till there's a lowest value in priority queue
            smallest = queue.get()[1]
            if smallest == end:  # at last stage
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                path.append(smallest)
                break  # there might be something so we'd stop looping
            if smallest or distance[smallest] != float("inf"):
                # getting all the neighbors of the current smallest node
                for neighbor_node, neighbor_weight in self.adjacency_list[smallest]:
                    # candidate nodes weight will be distance of smallest till now and neighbors weight
                    candidate_weight = distance[smallest] + neighbor_weight
                    # checking if smaller
                    if candidate_weight < distance[neighbor_node]:
                        distance[neighbor_node] = candidate_weight
                        # updating the prev to maintain the route
                        previous[neighbor_node] = smallest
                        # adding the new node to the p_queue
                        queue.put((candidate_weight, neighbor_node))

        return path[::-1]


graph = Dijkstra()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "E", 3)
graph.add_edge("C", "D", 2)
graph.add_edge("C", "F", 4)
graph.add_edge("D", "E", 3)
graph.add_edge("D", "F", 1)
graph.add_edge("E", "F", 1)

print(f"from A to E the path is ", graph.dijkstra_algo("A", "E"))
