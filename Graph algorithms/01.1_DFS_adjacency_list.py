# DFS - Depth First Search


# 1st solution

def DFS(graph, root):
    visited = [False] * len(graph)
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


graph = [[1, 8], [0], [3, 4, 5, 8], [2], [2, 7], [2, 6], [5, 8], [4, 6], [0, 2, 6]]

result1 = DFS(graph, 1)
print(result1)

result2 = dfs(graph, 1, [])
print(result2)
