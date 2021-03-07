def insertion_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return T


T = [5, 2, 4, 6, 1, 3]
print(insertion_sort(T))
