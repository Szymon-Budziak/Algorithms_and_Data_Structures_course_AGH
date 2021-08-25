# The internet cafe has K computers and A applications on CDs. Maximum one application can be installed
# on each computer. Each application has a list of computers on which it can run and the rest cannot, due
# to hardware requirements. We are the owner of a cafe and we know haw many customers (possibly zero) will
# would like to use the application tomorrow. We assume that each client occupies a computer for the
# whole day. What an application should we install on each of the computers so that all customers can use
# the application which they want. If there is not such an assignment, the algorithm should consider that.\
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


def internet_cafe(graph, computers, applications, demand_applications):
    size = len(computers) + len(applications) + 2
    new_graph = [[0] * size for _ in range(size)]
    for i in range(len(applications)):
        for j in range(len(graph[applications[i]])):
            new_graph[applications[i] + 1][graph[applications[i]][j] + 1] = 1
    for i in range(len(computers)):
        new_graph[computers[i] + 1][-1] = 1
    number_of_customers = 0
    for i in range(len(demand_applications)):
        number_of_customers += demand_applications[i][1]
        new_graph[0][demand_applications[i][0] + 1] = demand_applications[i][1]
    result = ford_fulkerson_algorithm(new_graph, 0, size - 1)
    if result == number_of_customers:
        return True
    return False


applications = [0, 1, 2, 3]
computers = [4, 5, 6, 7, 8]
demand_applications = [(0, 2), (1, 2), (3, 1)]
graph = [[4, 7], [5, 6, 7], [4, 7], [8]]
print(internet_cafe(graph, computers, applications, demand_applications))
