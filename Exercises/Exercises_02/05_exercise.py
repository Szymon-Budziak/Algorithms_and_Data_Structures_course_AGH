# Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
# czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.


def leader(A):
    maximum = max(A)
    buckets = [[0] for _ in range(len(A) + 1)]
    for i in range(len(A)):
        index = int((A[i] / maximum) * len(A))
        buckets[index].append(A[i])
        buckets[index][0] += 1
        if buckets[index][0] > len(A) // 2:
            return True
    return False


A = [12, 3, 5, 7, 7, 12, 7, 4, 10, 2, 7, 7, 7, 7, 7]
print(leader(A))
