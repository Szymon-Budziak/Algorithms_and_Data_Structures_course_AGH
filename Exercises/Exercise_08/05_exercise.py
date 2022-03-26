# Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym ujściem, jeśli:
#   (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz
#   (b) nie istnieje żadna krawędź wychodząca z t.
# Proszę podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej grafu.


# a) solution in O(n^2)


def universal_estuary(graph):
    result = []
    for i in range(len(graph)):
        all_zeros = True
        for j in range(len(graph)):
            if graph[i][j] == 1:
                all_zeros = False
                break
        if all_zeros:
            result.append(i)
    for u in result:
        all_ones = True
        for v in range(len(graph)):
            if u != v and graph[v][u] == 0:
                all_ones = False
        if all_ones:
            return u
    return False


# b) solution in O(n)


def universal_estuary2(graph):
    i = j = 0
    while i < len(graph) and j < len(graph):
        if graph[i][j] == 1:
            i += 1
        else:
            j += 1
    i = min(i, j)
    for k in range(len(graph)):
        if graph[i][k] != 0:
            return False
        if graph[k][i] != 1 and k != i:
            return False
    return i


graph = [[0, 0, 1, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]
print(universal_estuary(graph))
print(universal_estuary2(graph))
