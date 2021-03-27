from time import perf_counter
from random import randint, seed, shuffle
seed(100)


def insertion_sort(T):
    for i in range(len(T)):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return T


def median_of_medians(T, index):
    sublists = [T[j:j+5] for j in range(0, len(T), 5)]
    medians = [insertion_sort(sublist)[len(sublist)//2]
               for sublist in sublists]
    if len(medians) <= 5:
        pivot = insertion_sort(medians)[len(medians)//2]
    else:
        pivot = median_of_medians(medians, len(medians)//2)
    low = [i for i in T if i < pivot]
    high = [i for i in T if i > pivot]
    if index < len(low):
        return median_of_medians(low, index)
    elif index > len(low):
        return median_of_medians(high, index-len(low)-1)
    else:
        return pivot


T = list({randint(1, 10000) for _ in range(10000)})
shuffle(T)
start = perf_counter()
print(median_of_medians(T, 296))
end = perf_counter()
print(end-start)
