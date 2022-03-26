# Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program, który stwierdza
# czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.


def find_sum(T, x):
    i = 0
    j = len(T) - 1
    while i <= j:
        if T[i] + T[j] == x:
            return True
        elif T[i] + T[j] > x:
            j -= 1
        else:
            i += 1
    return False


T = [1, 3, 3, 5, 6, 7, 9, 9, 10, 12]
x = 16
print(find_sum(T, x))
