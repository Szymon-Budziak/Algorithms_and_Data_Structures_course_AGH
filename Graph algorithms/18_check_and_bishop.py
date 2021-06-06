# Algocia is placed on a great dessert and consists of cities and oases connected by roads. There is
# exactly one road leading from each gate to one oasis (but any given oasis can have any number of roads
# leading to them, oases can also be interconnected by roads). Algocian law requires that if someone
# enters a city through one gate, they must leave the other. Check of Algocia decided to send a bishop
# who will read the prohibition of formulating tasks "about the chessboard" (insult majesty) task in
# every city. Check wants the bishop to visit each city exactly once (but there is no limit how many
# times the bishop will visit each oasis). Bishop departs from the capital of Algocia city x, and after
# visiting all cities the bishop has to come back to city x. Find algorithm that determines if there
# is a suitable route for bishop.


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
