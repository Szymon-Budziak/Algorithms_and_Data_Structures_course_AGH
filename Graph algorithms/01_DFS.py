# DFS - Depth First Search


# 1st solution

def DFS(graph, root):
    visited = [False] * (len(graph) + 1)
    result = [root]

    def dfs_visit(u, graph, visited, result):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                result.append(v)
                dfs_visit(v, graph, visited, result)

    dfs_visit(root, graph, visited, result)
    return result


# 2nd solution

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


graph = {
    1: [2, 9],
    2: [2],
    3: [4, 5, 6, 9],
    4: [3],
    5: [3, 8],
    6: [3, 7],
    7: [6, 9],
    8: [5, 7],
    9: [1, 3, 7]
}

result1 = DFS(graph, 1)
print(result1)

result2 = dfs(graph, 1, [])
print(result2)
