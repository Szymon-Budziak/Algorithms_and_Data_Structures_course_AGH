# Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. Każde miasto
# jest otoczone murem i ma tylko dwie bramy: północną i południową. Z każdej bramy prowadzi dokładnie
# jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też być
# połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą,
# to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju
# odczyta zakaz formułowania zadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec
# odwiedził każde miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz).
# Goniec wyjeżdża ze stolicji Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić.
# Proszę przedstawić algorytm, który stwierdza czy odpowiednia trasa gońca istnieje. Proszę uzasadnić
# poprawność algorytmu oraz oszacować jego złożoność czasową.


def check_and_bishop(graph, oasis):
    changed_graph = []
    for i in range(len(graph)):
        if i not in oasis:
            changed_graph.append([graph[i][0], graph[i][1], 0])
        else:
            for j in range(len(graph[i])):
                if graph[i][j] in oasis:
                    if [graph[i][j], i, 1] not in changed_graph:
                        changed_graph.append([i, graph[i][j], 1])
    count = 0
    vertices = []
    for i in range(len(changed_graph)):
        if changed_graph[i][2] == 1:
            vertices.append((changed_graph[i][0], changed_graph[i][1]))
            count += 1
    for i in range(len(vertices)):
        for j in range(len(changed_graph)):
            if changed_graph[j][0] in vertices[i]:
                changed_graph[j][0] = min(vertices[i])
            if changed_graph[j][1] in vertices[i]:
                changed_graph[j][1] = min(vertices[i])
    i = 0
    while i < len(changed_graph):
        j = i + 1
        while j < len(changed_graph):
            if changed_graph[i][0] == changed_graph[j][0] and changed_graph[i][1] == changed_graph[j][1] and \
                    changed_graph[i][2] == 1:
                changed_graph.remove(changed_graph[i])
            elif changed_graph[i][0] == changed_graph[j][0] and changed_graph[i][1] == changed_graph[j][1] and \
                    changed_graph[j][2] == 1:
                changed_graph.remove(changed_graph[j])
            j += 1
        i += 1
    new_graph = []
    for i in range(len(changed_graph)):
        if changed_graph[i][0] not in new_graph:
            new_graph.append(changed_graph[i][0])
        if changed_graph[i][1] not in new_graph:
            new_graph.append(changed_graph[i][1])
    for i in range(len(new_graph)):
        new_graph[i] = [new_graph[i], 0]
    for i in range(len(new_graph)):
        for j in range(len(changed_graph)):
            if new_graph[i][0] == changed_graph[j][0]:
                new_graph[i][1] += 1
            if new_graph[i][0] == changed_graph[j][1]:
                new_graph[i][1] += 1
    for i in range(len(new_graph)):
        if new_graph[i][1] % 2 == 1:
            return False
    return True


oasis = [2, 4, 5, 7, 9]
graph = [[2, 4], [2, 9], [0, 4, 3], [2, 5], [0, 2, 6], [3, 7, 8], [4, 7], [5, 6, 8], [5, 7], [1]]
print(check_and_bishop(graph, oasis))
