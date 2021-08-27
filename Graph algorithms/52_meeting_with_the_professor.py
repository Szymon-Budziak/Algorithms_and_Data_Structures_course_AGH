# A famous professor invited you to a meeting in the Magic City. In this city some roads can only be used
# by people under the age of 30 (including us), others only by people over the age of 30 (including the
# professor). There are also roads that can be traveled by anyone. Each road has a certain length,
# expressed in a positive natural number, and roads can be one-way or two-way. These roads connect possible
# meeting locations. Among them, we distinguish your house and the professor's house. The professor asks
# us to choose a place for the meeting so that the total distance that we and the professor must travel
# is the smallest. If there is more than one such a place, list them all. If there is no such a place,
# the algorithm should consider that.
from queue import PriorityQueue
from math import inf


def relax(graph, u, v, distance):
    if distance[v] > distance[u] + graph[u][v]:
        distance[v] = distance[u] + graph[u][v]
        return True
    return False


def dijkstra_algorithm(graph, source):
    queue = PriorityQueue()
    queue.put((0, source))
    distance = [inf] * len(graph)
    distance[source] = 0
    visited = [False] * len(graph)
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(graph)):
            if graph[u][v] != 0 and not visited[v]:
                if relax(graph, u, v, distance):
                    queue.put((dist + graph[u][v], v))
        visited[u] = True
    return distance


def meeting_with_the_professor(under_thirty, over_thirty, normal, s, t):
    professor_graph = [[0] * (t + 1) for _ in range(t + 1)]
    student_graph = [[0] * (t + 1) for _ in range(t + 1)]
    for i in range(len(under_thirty)):
        student_graph[under_thirty[i][0]][under_thirty[i][1]] = under_thirty[i][2]
        student_graph[under_thirty[i][1]][under_thirty[i][0]] = under_thirty[i][2]
    for i in range(len(over_thirty)):
        professor_graph[over_thirty[i][0]][over_thirty[i][1]] = over_thirty[i][2]
        professor_graph[over_thirty[i][1]][over_thirty[i][0]] = over_thirty[i][2]
    for i in range(len(normal)):
        student_graph[normal[i][0]][normal[i][1]] = normal[i][2]
        student_graph[normal[i][1]][normal[i][0]] = normal[i][2]
        professor_graph[normal[i][0]][normal[i][1]] = normal[i][2]
        professor_graph[normal[i][1]][normal[i][0]] = normal[i][2]
    student_distance = dijkstra_algorithm(student_graph, s)
    professor_distance = dijkstra_algorithm(professor_graph, t)
    min_distance = [inf, None]
    for i in range(len(student_distance)):
        if student_distance[i] + professor_distance[i] < min_distance[0]:
            min_distance[0] = student_distance[i] + professor_distance[i]
            min_distance[1] = i
    return min_distance


under_thirty = [(0, 2, 2), (0, 4, 4), (1, 3, 1), (3, 7, 4), (8, 10, 5), (11, 12, 1)]
over_thirty = [(0, 1, 3), (0, 4, 4), (5, 6, 2), (6, 11, 2), (7, 8, 2), (9, 10, 2)]
normal = [(0, 1, 3), (2, 3, 5), (4, 5, 3), (7, 9, 1), (6, 9, 3), (10, 12, 4)]
student_house = 0
professor_house = 12
print(meeting_with_the_professor(under_thirty, over_thirty, normal, student_house, professor_house))
