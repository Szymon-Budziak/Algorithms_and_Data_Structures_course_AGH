# Vasya takes part in the orienteering competition. There are n checkpoints located along the
# line at coordinates x[1], x[2], ..., x[n]. Vasya starts at the point with coordinate a. His
# goal is to visit at least n-1 checkpoint in order to finish the competition. Participant
# are allowed to visit checkpoints in arbitrary order. Vasya wants to pick such checkpoints and
# the order of visiting them that the total distance travelled is minimized. He asks you to
# calculate this minimum possible value.

def heapify(T, heap_size, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heap_size and T[i] < T[l]:
        largest = l
    if r < heap_size and T[largest] < T[r]:
        largest = r
    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        heapify(T, heap_size, largest)


def heapsort(T):
    heap_size = len(T)
    for i in range(heap_size // 2, -1, -1):
        heapify(T, heap_size, i)
    for j in range(heap_size - 1, 0, -1):
        T[j], T[0] = T[0], T[j]
        heapify(T, j, 0)


def checkpoints(n, a, T):
    if n == 1:
        return 0
    heapsort(T)
    distance_1 = abs(T[0] - T[n - 2])
    distance_2 = abs(T[1] - T[n - 1])
    dist_to_0 = abs(a - T[0])
    dist_to_1 = abs(a - T[1])
    dist_to_n1 = abs(a - T[n - 1])
    dist_to_n2 = abs(a - T[n - 2])
    return min(distance_1 + dist_to_0, distance_1 + dist_to_n2,
               distance_2 + dist_to_1, distance_2 + dist_to_n1)


n = 9
a = -3
T = [-10, -7, -3, -4, 7, -6, 10, -10, -7]
print(checkpoints(n, a, T))
