# Proszę zaimplementować sortowanie tablicy w czasie O(n^2).


def insertion_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return T


T = [5, 4, 3, 7, 2, 1]
print(insertion_sort(T))
