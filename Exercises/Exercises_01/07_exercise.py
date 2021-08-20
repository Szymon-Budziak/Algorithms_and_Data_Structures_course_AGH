# Dana jest posortowana tablica A[1, ..., n] oraz liczba x. Proszę napisać program, który stwierdza
# czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.


def sum_search(T, x):
    l = 0
    r = len(T) - 1
    while l < r:
        if T[l] + T[r] == x:
            return True
        elif T[l] + T[r] > x:
            r -= 1
        else:
            l += 1
    return False


T = [2, 5, 8, 12, 16, 19, 20, 25, 34, 55, 81]
x = 37
print(sum_search(T, x))
