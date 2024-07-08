import heapq


def most_reliable_path(graph, source, target):
    R = {v: 0 for v in graph}
    R[source] = 1
    pq = [(-1, source)]

    while pq:
        current_reliability, u = heapq.heappop(pq)
        current_reliability = -current_reliability

        if u == target:
            return current_reliability

        for v, weight in graph[u].items():
            new_reliability = current_reliability * weight
            if new_reliability > R[v]:
                R[v] = new_reliability
                heapq.heappush(pq, (-new_reliability, v))

    return R[target]


graph = {"a": {"b": 0.9, "c": 0.8}, "b": {"d": 0.7}, "c": {"d": 0.6}, "d": {}}

source = "a"
target = "d"
print(most_reliable_path(graph, source, target))
