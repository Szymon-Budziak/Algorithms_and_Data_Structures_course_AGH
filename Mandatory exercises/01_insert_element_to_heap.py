from math import inf


def heap_increase_key(T, i, key):
    if key < T[i]:
        return False
    T[i] = key
    while i > 1 and T[(i-1)//2] < T[i]:
        T[i], T[(i-1)//2] = T[(i-1)//2], T[i]
        i = (i-1)//2


def heap_insert(T, key):
    T += [-inf]
    print(len(T))
    heap_increase_key(T, len(T)-1, key)
    return T


def max_heapify(T, heap_size, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < heap_size and T[l] > T[i]:
        largest = l
    if r < heap_size and T[r] > T[largest]:
        largest = r
    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        max_heapify(T, heap_size, largest)


def build_max_heap(T, heap_size):
    for i in range(len(T)//2, -1, -1):
        max_heapify(T, heap_size, i)


T = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
heap_insert(T, 11)
build_max_heap(T, len(T))
print(T)
