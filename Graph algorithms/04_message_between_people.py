# Given list of people who know each other. People are represented as number between 0 and n-1.
# First day person 0 passes the message to all his friends. Second day each friend passes this
# message to all their friends who doesn't know this message and so on. Find algorithm that
# returns the day when the most people knew the message and the number of people who received it
# that day.
from queue import Queue


def message(graph, source):
    queue = Queue()
    visited = [False] * len(graph)
    visited[source] = True
    queue.put(source)
    max_people = day = 0
    count = 1
    prev_people = 1
    while not queue.empty():
        people = 0
        for i in range(prev_people):
            u = queue.get()
            for v in graph[u]:
                if not visited[v]:
                    queue.put(v)
                    visited[v] = True
                    people += 1
        count += 1
        if people > max_people:
            max_people = people
            day = count
        prev_people = people
    return day, max_people


graph = [[1, 2], [0, 3, 4], [0, 5, 6], [1, 10], [1, 5, 7, 8, 7, 9, 11],
         [2, 4, 6], [2, 5], [4], [4], [4], [3], [4]]
print(message(graph, 0))
