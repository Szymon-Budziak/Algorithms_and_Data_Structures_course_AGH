# Alice wants to give a party and wonders who to invite from among the n friends. She has already
# created a list of pairs of people who know each other. She wants to select as many people as possible,
# so that at the party, each pearson should know at least x people and at least x people not to know.
# Write an algorithm that takes a list of n people and a list of pairs of people who know each other.
# Find the longest possible list of guests.


# 1st solution: greedy


def remove_guests(T, x, n):
    for i in range(len(T)):
        if (T[i][-2] < x or T[i][-2] > len(guests) - x) and T[i][-2] > 0:
            for j in range(len(T[0]) - 2):
                if T[i][j] == 1:
                    T[i][j], T[j][i] = 0, 0
                    T[i][-2] -= 1
                    T[i][-1] += 1
                    T[j][-2] -= 1
                    T[j][-1] += 1
                if T[i][-2] == 0:
                    break
            remove_guests(T, x, n)


def party_with_friends(guests, x):
    n = len(guests)
    T = [[0] * (len(guests) + 2) for _ in range((len(guests)))]
    for i in range(len(T)):
        T[i][i] = 0
    for i in range(len(guests)):
        for j in range(len(guests[i])):
            T[i][guests[i][j]] = 1
            T[guests[i][j]][i] = 1
    for i in range(len(T)):
        T[i][-2] = T[i].count(1)
        T[i][-1] = T[i].count(0) - 2
    remove_guests(T, x, n)
    count = 0
    for i in range(len(T)):
        if T[i][-2] >= x and T[i][-2] <= len(guests) - x:
            count += 1
    return count


# 2nd solution: graph


def party_with_friends_graph(graph, x):
    n = len(guests)
    T = [0] * len(graph)
    for i in range(len(graph)):
        T[i] = len(graph[i])
    visited = [False] * len(graph)
    dfs(graph, 0, visited, T, x)
    count = 0
    for i in range(len(T)):
        if T[i] >= x and T[i] <= n - x:
            count += 1
    return count


def dfs(graph, source, visited, T, x):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, T, x)
    if T[source] < x or T[source] > len(graph) - x:
        i = 0
        while i < len(graph[source]):
            T[source] -= 1
            T[graph[source][i]] -= 1
            graph[graph[source][i]].remove(source)
            graph[source].remove(graph[source][i])


x = 2
guests = [[1, 4, 5, 7],
          [0, 3, 5, 6, 7],
          [3],
          [1, 2],
          [0],
          [0, 1],
          [1, 8],
          [1, 0],
          [6]]
print(party_with_friends(guests, x))
print(party_with_friends_graph(guests, x))
