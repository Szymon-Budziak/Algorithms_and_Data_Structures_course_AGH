# After a terrifying forest fire in Berland a forest rebirth program was carried out. Due to it N rows
# with M trees each were planted and the rows were so neat that one could map it on a system of
# coordinates so that the j-th tree in the i-th row would have the coordinates of (i, j). However
# a terrible thing happened and the young forest caught fire. Now we must find the coordinates of the
# tree that will catch fire last to plan evacuation. The burning began in K points simultaneously,
# which means that initially K trees started to burn. Every minute the fire gets from the burning
# trees to the ones that aren’t burning and that the distance from them to the nearest burning tree
# equals to 1. Find the tree that will be the last to start burning. If there are several such trees,
# output any.
from queue import Queue


def fire_again(N, M, K, T):
    graph = [[0] * (M + 1) for _ in range(N + 1)]
    queue = Queue()
    for i in range(0, 2 * K - 1, 2):
        graph[T[i]][T[i + 1]] = 1
        queue.put((T[i], T[i + 1]))
    x, y = 0, 0
    while not queue.empty():
        x, y = queue.get()
        x_moves = [x - 1, x + 1, x, x]
        y_moves = [y, y, y - 1, y + 1]
        for i in range(len(x_moves)):
            if 0 < x_moves[i] <= N and 0 < y_moves[i] <= M:
                if graph[x_moves[i]][y_moves[i]] == 0:
                    x = x_moves[i]
                    y = y_moves[i]
                    graph[x_moves[i]][y_moves[i]] = 1
                    queue.put((x_moves[i], y_moves[i]))
    return x, y


N = 10
M = 10
K = 2
T = [7, 8, 1, 9]
print(fire_again(N, M, K, T))
