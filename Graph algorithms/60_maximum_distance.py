# Chouti was tired of the tedious homework, so he opened up an old programming problem he created
# years ago. You are given a connected undirected graph with n vertices and m weighted edges. There
# are k special vertices: x1, x2, ..., xk. Let's define the cost of the path as the maximum weight of
# the edges in it. And the distance between two vertexes as the minimum cost of the paths connecting
# them. For each special vertex, find another special vertex which is farthest from it (in terms of
# the previous paragraph, i.e. the corresponding distance is maximum possible) and output the
# distance between them. The original constraints are really small so he thought the problem was
# boring. Now, he raises the constraints and hopes you can solve it for him.


def find(x, parent):
    actual = []
    while parent[x] != x:
        actual.append(x)
        x = parent[x]
    for i in range(len(actual)):
        parent[actual[i]] = x
    return x


def union(x, y, visited, parent):
    x = find(x, parent)
    y = find(y, parent)
    if visited[y]:
        x, y = y, x
    parent[y] = x


def kruskal(edges, parent, visited):
    best_value = 0
    for i in range(len(edges)):
        x = find(edges[i][0], parent)
        y = find(edges[i][1], parent)
        if x == y:
            continue
        if visited[x] and visited[y]:
            best_value = max(best_value, edges[i][2])
        union(edges[i][0], edges[i][1], visited, parent)
    return best_value


def maximum_distance(n, m, k, special, edges):
    visited = [False] * (n + 1)
    for i in range(len(special)):
        visited[special[i]] = True
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    best_value = kruskal(edges, parent, visited)
    for i in range(k):
        print(best_value, end=" ")


n = 5
m = 7
k = 4
special = [1, 2, 3, 4]
edges = [(1, 2, 3), (5, 1, 4), (3, 1, 1), (4, 2, 5), (2, 5, 6), (2, 3, 3), (3, 4, 6)]
maximum_distance(n, m, k, special, edges)
