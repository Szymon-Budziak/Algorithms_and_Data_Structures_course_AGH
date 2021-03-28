# Proszę zaimplementować funkcję: def sum_between(T, p, r). Zadaniem tej funkcji jest
# obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej tablicy znajdywałyby
# się na pozycjach o indeksach od p do r(włącznie). Można przyjąć, że liczby w tablicy T są
# parami różne(ale nie można przyjmować żadnego innego rozkładu danych). Zaimplementowana
# funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność czasową
# (oraz bardzo krótko uzasadnić to oszacowanie).


def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quick_select(T, p, r, x):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if x == q:
        return T[x]
    elif x > q:
        return quick_select(T, q+1, r, x)
    else:
        return quick_select(T, p, q-1, x)


def sum_between(T, index1, index2):
    quick_select(T, 0, len(T)-1, index1)
    quick_select(T, 0, len(T)-1, index2)
    # Complexity of quick select in average case is O(n), n length of array,
    # so complexity of two quick selects is 2*O(n)
    summary = 0
    for i in range(index1, index2+1):
        summary += T[i]
    # Complexity if this loop is O(n)
    # Complexity of the whole algorithm is 2*O(n) + O(n) = 3*O(n) == O(n)
    return summary


T = [23, 8, 34, 7, 2, 15, 22, 18, 36, 31, 19, 9, 2, 4]
print(sum_between(T, 3, 12))
