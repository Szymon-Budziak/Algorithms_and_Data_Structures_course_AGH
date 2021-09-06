# Dany jest zbiór przedziałów A = {(a[0], b[0]), ..., (a[n−1], b[n−1])}. Proszę zaimplementować funkcję:
# def kintersect(A, k):
#     ...
# która wyznacza k przedziałów, których przecięcie jest jak najdłuższym przedziałem. Zbiór A jest
# reprezentowany jako lista par. Końce przedziałów to liczby całkowite. Można założyć, że k ≥ 1 oraz
# k jest mniejsze lub równe łącznej liczbie przedziałów w A. Funkcja powinna zwracać listę numerów
# przedziałów, które należą do rozwiązania.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.
from Exercise_3_tests import runtests


def kintersect(A, k):
    interval = [(i, A[i][0], A[i][1]) for i in range(len(A))]
    interval.sort(key=lambda x: x[2], reverse=True)
    max_length = 0
    if k == 1:
        result = [0]
        for i in range(len(A)):
            if interval[i][2] - interval[i][1] > max_length:
                max_length = interval[i][2] - interval[i][1]
                result[0] = interval[i][0]
        return result
    result = []
    for i in range(len(A)):
        current = [interval[i][0]]
        for j in range(len(A)):
            if i != j and interval[j][1] <= interval[i][1] < interval[j][2]:
                current.append(interval[j][0])
                if len(current) == k:
                    actual_length = min(interval[j][2] - interval[i][1], interval[i][2] - interval[i][1])
                    if actual_length > max_length:
                        max_length = actual_length
                        result.clear()
                        result = [current[i] for i in range(k)]
                    break
    return result


runtests(kintersect)
