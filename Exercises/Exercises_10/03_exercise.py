# Dana jest formuła logiczna w postaci 2CNF. To znaczy, że formuła jest koniunkcją klauzuli, gdzie
# każda klauzula to alternatywa dwóch literałów, a każdy literał to zmienna lub jej negacja. Przykładem
# formuły w postaci 2CNF nad zmiennymi x,y,z jest:
# (x v y) ∧ (~x v z) ∧ (~z v ~y).
# Proszę podać algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartościowanie
# spełniające formułę.


def SCC(graph):
    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            DFSUtil(graph, i, visited, stack)
    new_graph = [[] for _ in range(len(graph))]
    transpose_graph(graph, new_graph)
    for j in range(len(visited)):
        visited[j] = False
    result = [[] for _ in range(len(graph))]
    index = 0
    while len(stack):
        u = stack.pop()
        if not visited[u]:
            dfs(new_graph, u, visited, result, index)
            index += 1
    return result


def dfs(graph, source, visited, result, index):
    visited[source] = True
    result[index].append(source)
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result, index)


def DFSUtil(graph, source, visited, stack):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DFSUtil(graph, v, visited, stack)
    stack.append(source)


def transpose_graph(graph, new_graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            new_graph[graph[i][j]].append(i)


def two_sat_problem(formula):
    variables = []
    for i in range(len(formula)):
        if formula[i] == "(":
            j = i + 1
            while formula[j] != ")":
                if formula[j] != " " and formula[j] != "v":
                    variables.append(formula[j])
                j += 1
    i = 0
    while i != len(variables):
        if variables[i] == "~":
            variables[i] = variables[i] + variables[i + 1]
            variables.pop(i + 1)
        i += 1
    variables.sort()
    new_variables = []
    for i in range(0, len(variables), 2):
        if "~" not in variables[i]:
            new_variables.append(("~" + variables[i], variables[i + 1]))
        else:
            new_variables.append((variables[i][1], variables[i + 1]))
        if "~" not in variables[i + 1]:
            new_variables.append(("~" + variables[i + 1], variables[i]))
        else:
            new_variables.append((variables[i + 1][1], variables[i]))
    graph_vertices = []
    for i in range(len(new_variables)):
        if new_variables[i][0] not in graph_vertices:
            graph_vertices.append(new_variables[i][0])
        if new_variables[i][1] not in graph_vertices:
            graph_vertices.append(new_variables[i][1])
    graph = [[] for _ in range(len(graph_vertices))]
    for i in range(len(new_variables)):
        index_1 = variables.index(new_variables[i][0])
        index_2 = variables.index(new_variables[i][1])
        graph[index_1].append(index_2)
    result = SCC(graph)
    for i in range(len(result)):
        if len(result[i]) > 0:
            check = [False] * len(variables)
            for j in range(len(result[i])):
                check[result[i][j]] = True
            for j in range(len(variables)):
                if "~" not in variables[j]:
                    idx = variables.index("~" + variables[j])
                    if check[j] and check[idx]:
                        return False
    return True


formula = "(x v y) ∧ (~x v z) ∧ (~z v ~y)"
print(two_sat_problem(formula))
