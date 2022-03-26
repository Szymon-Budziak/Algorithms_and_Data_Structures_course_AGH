# Proszę zaproponować algorytm scalający k posortowanych list.


def heapify(T, heap_size, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heap_size and T[l][0] < T[smallest][0]:
        smallest = l
    if r < heap_size and T[r][0] < T[smallest][0]:
        smallest = r
    if smallest != i:
        T[i], T[smallest] = T[smallest], T[i]
        heapify(T, heap_size, smallest)


def build_max_heap(T):
    heap_size = len(T)
    for i in range(heap_size // 2, -1, -1):
        heapify(T, heap_size, i)


def insert(T, key, index):
    T.append((key, index))
    i = len(T) - 1
    while i > 0 and T[(i - 1) // 2][0] > key:
        T[i], T[(i - 1) // 2] = T[(i - 1) // 2], T[i]
        i = (i - 1) // 2
    return T


def merge_k_lists(T):
    heap = [(T[i][0], i) for i in range(len(T))]
    build_max_heap(heap)
    result = []
    while len(heap) != 0:
        min_value, index = heap.pop(0)
        heapify(heap, len(heap) - 1, 0)
        result.append(min_value)
        T[index].pop(0)
        if len(T[index]) != 0:
            insert(heap, T[index][0], index)
    return result


T = [[3, 17, 24, 49], [2, 5], [31, 52], [8, 8, 27]]
print(merge_k_lists(T))
