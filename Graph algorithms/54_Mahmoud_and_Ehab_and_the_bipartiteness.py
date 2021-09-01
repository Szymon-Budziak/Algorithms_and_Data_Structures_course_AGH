# Mahmoud and Ehab continue their adventures! As everybody in the evil land knows, Dr. Evil likes
# bipartite graphs, especially trees. A tree is a connected acyclic graph. A bipartite graph is a graph,
# whose vertices can be partitioned into 2 sets in such a way, that for each edge (u, v) that belongs
# to the graph, u and v belong to different sets. Dr. Evil gave Mahmoud and Ehab a tree consisting of
# n nodes and asked them to add edges to it in such a way, that the graph is still bipartite. Besides,
# after adding these edges the graph should be simple (doesn't contain loops or multiple edges).
# What is the maximum number of edges they can add?
from queue import Queue


def Mahmoud_and_Ehab_and_the_bipartiteness(n, T):
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        u, v = T[i]
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    queue = Queue()
    distance = [-1] * n
    for i in range(n):
        if distance[i] == -1:
            distance[i] = 0
            queue.put(i)
            while not queue.empty():
                u = queue.get()
                for v in graph[u]:
                    if distance[v] == -1:
                        distance[v] = 1 - distance[u]
                        queue.put(v)
    left = distance.count(0)
    right = n - left
    return left * right - (n - 1)


n = 10
T = [(7, 6), (2, 7), (4, 1), (8, 5), (9, 4), (5, 3), (8, 7), (10, 8), (10, 4)]
print(Mahmoud_and_Ehab_and_the_bipartiteness(n, T))
