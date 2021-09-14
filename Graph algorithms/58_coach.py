# A programming coach has n students to teach. We know that n is divisible by 3. Let's assume that
# all students are numbered from 1 to n, inclusive. Before the university programming championship
# the coach wants to split all students into groups of three. For some pairs of students we know that
# they want to be on the same team. Besides, if the i-th student wants to be on the same team with
# the j-th one, then the j-th student wants to be on the same team with the i-th one. The coach wants
# the teams to show good results, so he wants the following condition to hold: if the i-th student
# wants to be on the same team with the j-th, then the i-th and the j-th students must be on the
# same team. Also, it is obvious that each student must be on exactly one team. Help the coach and
# divide the teams the way he wants.


def dfs(graph, u, visited, actual_team):
    if not visited[u]:
        actual_team.append(u)
    visited[u] = True
    for v in range(len(graph)):
        if not visited[v] and graph[u][v] == 1:
            dfs(graph, v, visited, actual_team)


def coach(n, m, T):
    graph = [[0] * n for _ in range(n)]
    for i in range(m):
        a, b = T[i]
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = 1
    teams = [[], [], []]
    visited = [False] * len(graph)
    flag = False
    for i in range(len(graph)):
        actual_team = []
        dfs(graph, i, visited, actual_team)
        if len(actual_team) >= 4:
            flag = True
            break
        elif len(actual_team) > 0:
            teams[len(actual_team) - 1].append(actual_team)
    if flag or (not flag and len(teams[1]) > len(teams[0])):
        print(-1)
    else:
        for i in range(len(teams[2])):
            print(teams[2][i][0] + 1, teams[2][i][1] + 1, teams[2][i][2] + 1)
        idx = 0
        for i in range(len(teams[1])):
            print(teams[1][i][0] + 1, teams[1][i][1] + 1, teams[0][idx][0] + 1)
            idx += 1
        count = 0
        for i in range(idx, len(teams[0])):
            if count == 3:
                count = 0
                print('\n')
            print(teams[0][i][0] + 1, end=" ")
            count += 1


n = 18
m = 12
T = [(1, 10), (2, 4), (2, 8), (3, 15), (3, 18), (4, 8), (5, 6), (9, 13),
     (12, 14), (12, 16), (14, 16), (15, 18)]
coach(n, m, T)
