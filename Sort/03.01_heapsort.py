from time import perf_counter
from random import randint, seed
seed(100)


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


def heapsort(T):
    heap_size = len(T)
    build_max_heap(T, heap_size)
    for i in range(len(T)-1, -1, -1):
        T[0], T[i] = T[i], T[0]
        heap_size -= 1
        max_heapify(T, heap_size, 0)


T = [randint(1, 1000) for _ in range(10000)]
start = perf_counter()
heapsort(T)
print(T)
end = perf_counter()
print(end-start)
