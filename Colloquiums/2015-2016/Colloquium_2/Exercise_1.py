# Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest możliwa
# sekwencja ruchów spełniająca:
# - każdy ruch kończy się zbiciem skoczka,
# - sekwencja kończy się gdy zostanie jeden skoczek.


def dfs(graph, T, u):
    T[u[0]][u[1]] = 0
    for v in graph[u[0]][u[1]]:
        if T[v[0]][v[1]] == 1:
            dfs(graph, T, v)


def possible_moves(T, graph, x, y):
    new_x = [x + 2, x + 1, x - 1, x - 2, x - 2, x - 1, x + 1, x + 2]
    new_y = [y + 1, y + 2, y + 2, y + 1, y - 1, y - 2, y - 2, y - 1]
    for i in range(len(new_x)):
        if new_x[i] >= 0 and new_y[i] >= 0 and new_x[i] < len(T) and new_y[i] < len(T):
            if T[new_x[i]][new_y[i]] == 1:
                graph[x][y].append((new_x[i], new_y[i]))


def knights_moves(T):
    graph = [[[] for _ in range(len(T))] for _ in range(len(T))]
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] == 1:
                possible_moves(T, graph, i, j)
    dfs(graph, T, (0, 0))
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] == 1:
                return False
    return True


T = [[1, 1, 1, 1, 1, 0, 1, 0],
     [1, 1, 0, 0, 1, 0, 1, 1],
     [0, 1, 1, 1, 0, 1, 1, 1],
     [1, 0, 1, 0, 1, 1, 0, 1],
     [0, 0, 1, 0, 1, 1, 0, 0],
     [1, 1, 1, 0, 1, 1, 0, 1],
     [0, 1, 1, 0, 0, 0, 1, 0],
     [1, 1, 0, 0, 0, 0, 1, 0]]
print(knights_moves(T))
