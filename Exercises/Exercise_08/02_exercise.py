# Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj algorytm, który stwierdza czy
# w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że graf reprezentowany jest
# przez macierz sasiedztwa A.


def four_length_cycle(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j:
                count = 0
                result = []
                for k in range(len(graph)):
                    if graph[i][k] == 1 and graph[j][k] == 1:
                        count += 1
                        result.append(k)
                    if count >= 2:
                        result.append(i)
                        result.append(j)
                        return True, result
    return None, None


graph = [[0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [1, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 1, 1],
         [0, 0, 0, 0, 1, 0]]
decision, result = four_length_cycle(graph)
print(decision)
print(result)
