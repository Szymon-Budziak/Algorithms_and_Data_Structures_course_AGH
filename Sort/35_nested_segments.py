# You are given a sequence a[1], a[2], ..., a[n] of one-dimensional segments numbered 1 through n.
# Your task is to find two distinct indices i and j such that segment a[i] lies within segment a[j].
# Segment [l1, r1] lies within segment [l2, r2] if l1 >= l2 and r1 <= r2. Return indices i and j.
# If there are multiple answers, print any of them. If no answer exists, return -1, -1.


def partition(T, p, r):
    pivot = T[r][0]
    i = p - 1
    for j in range(p, r):
        if T[j][0] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, p, r):
    if len(T) == 1:
        return T
    if p < r:
        q = partition(T, p, r)
        quicksort(T, p, q - 1)
        quicksort(T, q + 1, r)


def nested_segments(n, T):
    for i in range(n):
        T[i] = (T[i][0], T[i][1], i + 1)
    quicksort(T, 0, len(T) - 1)
    for i in range(1, n):
        l1, r1, idx1 = T[i - 1]
        l2, r2, idx2 = T[i]
        if l1 <= l2 and r1 >= r2:
            return idx2, idx1
        elif l1 == l2 and r1 < r2:
            return idx1, idx2
    return -1, -1


n = 11
T = [(22226, 28285), (9095, 23314), (19162, 25530), (255, 13298), (4904, 25801), (17914, 23501),
     (8441, 28117), (11880, 29994), (11123, 19874), (21505, 27971), (7658, 14109)]
print(nested_segments(n, T))
