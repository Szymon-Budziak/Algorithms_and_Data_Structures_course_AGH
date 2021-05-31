# Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag). Proszę zaimplementować
# algorytm, który oblicza domknięcie przechodnie grafu G (domknięcie przechodnie grafu G to taki graf H,
# że w H mamy krawędź z u do v wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v).


def transitive_closure(graph):
    reach = [[0] * len(graph) for _ in range(len(graph))]
    for i in range(len(reach)):
        for j in range(len(reach)):
            if i == j:
                reach[i][j] = 1
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if graph[u][v] == 1 or (graph[u][k] == 1 and graph[k][v] == 1):
                    reach[u][v] = 1
    return reach


graph = [[0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0]]
reach = transitive_closure(graph)
for i in range(len(reach)):
    print(reach[i])
