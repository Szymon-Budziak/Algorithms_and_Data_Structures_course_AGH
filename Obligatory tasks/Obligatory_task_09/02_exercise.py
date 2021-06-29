# W jaki sposób znaleźć maksymalny przepływ w sieci w której możliwe jest kilka ujść i kilka źródeł.
from queue import Queue
from math import inf


def bfs(graph, s, t, parent):
    queue = Queue()
    visited = [False] * len(graph)
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return visited[t]


def ford_fulkerson_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


def multiple_source_and_sinks(graph, source, sink):
    source_count = sink_count = 0
    for i in range(len(source)):
        source_count += 1
    for i in range(len(sink)):
        sink_count += 1
    new_graph = [[0] * len(graph) for _ in range(len(graph))]
    start_source = min(source)
    end_sink = min(sink)
    for i in range(len(source)):
        for j in range(len(graph)):
            if graph[source[i]][j] != 0 and j not in source and j not in sink:
                new_graph[start_source][j] = graph[source[i]][j]
            elif j in sink and graph[i][j] != 0:
                new_graph[start_source][end_sink] = graph[source[i]][j]
    for i in range(len(sink)):
        for j in range(len(graph)):
            if graph[sink[i]][j] != 0 and j not in sink and j not in source:
                new_graph[end_sink][j] = graph[sink[i]][j]
            elif j in source:
                new_graph[end_sink][start_source] = graph[sink[i]][j]
    for i in range(len(graph)):
        if i in source or i in sink:
            continue
        for j in range(len(graph)):
            if j not in source and j not in sink and graph[i][j] != 0:
                new_graph[i][j] = graph[i][j]
            elif j in source and graph[i][j] != 0:
                new_graph[i][start_source] = graph[i][j]
            elif j in sink and graph[i][j] != 0:
                new_graph[i][end_sink] = graph[i][j]
    max_flow = ford_fulkerson_algorithm(new_graph, start_source, end_sink)
    return max_flow


graph = [[0, 10, 0, 8, 0, 0, 0],
         [0, 0, 11, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 4, 0],
         [0, 5, 0, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 12],
         [0, 0, 0, 0, 11, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
source = [0, 1, 2]
sink = [5, 6]
print(multiple_source_and_sinks(graph, source, sink))
