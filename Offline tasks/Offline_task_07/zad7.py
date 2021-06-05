from copy import deepcopy


def euler(G):
    for i in range(len(G)):
        edges = 0
        for j in range(len(G)):
            if G[i][j] == 1:
                edges += 1
        if edges % 2 == 1:
            return None
    result = []
    graph = deepcopy(G)
    dfs(graph, 0, result)
    result.reverse()
    return result


def dfs(graph, source, result):
    for i in range(len(graph)):
        if graph[source][i] == 1:
            graph[source][i] = graph[i][source] = 0
            dfs(graph, i, result)
    result.append(source)


# sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera funkcja zwraca prawidłowy wynik)


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
