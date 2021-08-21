# Proszę zaimplementować algorytm QuickSort bez użycia rekurencji (ale można wykorzystać własny
# stos; iteracyjnie).

def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def iterative_quicksort(T):
    S = []
    p = 0
    r = len(T) - 1
    S.append((p, r))
    while len(S) > 0:
        (p, r) = S.pop()
        if p < r:
            q = partition(T, p, r)
            if q - p > r - 1:
                S.append((p, q - 1))
                S.append((q + 1, r))
            else:
                S.append((q + 1, r))
                S.append((p, q - 1))
    return T


T = [38, 19, 7, 28, 23, 36, 3, 9, 6, 4, 22, 24, 17, 38, 35]
print(iterative_quicksort(T))
