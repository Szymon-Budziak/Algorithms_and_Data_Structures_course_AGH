# Given 2D array [N][N] in which each cell has the value "W" representing water or "L"
# representing land. Lake is a group of water cells connected by their banks. Count how
# many lakes are in array and how many cells has the biggest lake.


def dfs(T, visited, row, col, size):
    if row < 0 or row >= len(T) or col < 0 or col >= len(T) or T[row][col] == "L" or visited[row][col] == 1:
        return size
    else:
        size += 1
        visited[row][col] = 1
    actual_size = size
    actual_size = dfs(T, visited, row - 1, col, actual_size)
    actual_size = dfs(T, visited, row, col - 1, actual_size)
    actual_size = dfs(T, visited, row, col + 1, actual_size)
    actual_size = dfs(T, visited, row + 1, col, actual_size)
    return actual_size


def lakes(T):
    visited = [[-1] * len(T) for _ in range(len(T))]
    count = max_lake = 0
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] == "W" and visited[i][j] == -1:
                count += 1
                max_lake = max(dfs(T, visited, i, j, 0), max_lake)
    return count, max_lake


T = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "L", "W", "W"],
     ["W", "W", "L", "W", "W", "L", "W", "L"],
     ["L", "L", "L", "W", "L", "L", "L", "L"]]

print(lakes(T))
