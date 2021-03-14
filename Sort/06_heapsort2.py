from time import perf_counter
from random import randint, seed
seed(100)


def heapify(T, heap_size, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < heap_size and T[i] < T[l]:
        largest = l
    if r < heap_size and T[largest] < T[r]:
        largest = r
    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        heapify(T, heap_size, largest)


def heapsort(T):
    heap_size = len(T)
    for i in range(heap_size//2, -1, -1):
        heapify(T, heap_size, i)
    for j in range(heap_size-1, 0, -1):
        T[j], T[0] = T[0], T[j]
        heapify(T, j, 0)


T = [randint(1, 1000) for _ in range(10000)]
start = perf_counter()
heapsort(T)
print(T)
end = perf_counter()
print(end-start)
