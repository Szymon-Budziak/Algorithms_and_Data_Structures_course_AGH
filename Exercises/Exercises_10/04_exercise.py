# Król Bitocji postanowił zorganizować serię wyścigów samochodowych. Wyścigi mają się odbywać po trasach
# zamkniętych, składających się z odcinków autostrady łączących miasta Bitocji. Król chce, żeby każde
# miasto było zaangażowane w dokładnie jeden wyścig. W tym celu należy sprawdzić, czy da się wynająć
# odpowiednie odcinki autostrad. Należy jednak pamiętać o następujących ograniczeniach:
#   1) w Bitocji wszystkie autostrady są jednokierunkowe,
#   2) z każdego miasta wychodzą co najwyżej dwa odcinki autostrady, którymi można dojechać do innych
# miast,
#   3) do każdego miasta dochodzą co najwyżej dwa odcinki autostrady, którymi można przyjechać z innych
# miast.
# Proszę zaproponować algorytm, który mając na wejściu opis sieci autostrad Bitocji sprawdza czy da się
# zorganizować serię wyścigów tak, żeby przez każde miasto przebiegała trasa dokładnie jednego.


def detect_cycle(graph, source):
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    return dfs(graph, source, visited, parent)


def dfs(graph, source, visited, parent):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            parent[v] = source
            return dfs(graph, v, visited, parent)
        elif visited[v] and parent[source] != v:
            return True
    return False


def racing(graph):
    in_out = [[] for _ in range(len(graph))]
    in_count = [0] * len(graph)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            in_count[graph[i][j]] += 1
    for i in range(len(graph)):
        if in_count[i] == 2:
            in_out[i].append(0)
        if len(graph[i]) == 2:
            in_out[i].append(1)
    for i in range(len(graph)):
        if in_count[i] == 0 or len(in_out[i]) == 0:
            return False
    to_remove = []
    for i in range(len(graph)):
        if len(in_out[i]) > 1:
            for j in graph[i]:
                if len(in_out[j]) > 1 and 1 in in_out[i] and 0 in in_out[j]:
                    to_remove.append((i, j))
    for i in range(len(to_remove)):
        graph[to_remove[i][0]].remove(to_remove[i][1])
        in_out[to_remove[i][0]].remove(1)
        in_out[to_remove[i][1]].remove(0)
    to_remove = []
    for i in range(len(graph)):
        if 1 in in_out[i]:
            for j in graph[i]:
                if 0 in in_out[j]:
                    to_remove.append((i, j))
    for i in range(len(to_remove)):
        graph[to_remove[i][0]].remove(to_remove[i][1])
    return detect_cycle(graph, 0)


graph = [[2, 5],
         [0],
         [1, 4],
         [1],
         [3, 5],
         [0, 3]]
print(racing(graph))
