# We are given an array A an the number k. Find algorithm of distinct pairs of elements from
# array A with the difference of k. Example: for an array [7, 11, 3, 7, 3, 9, 5] and k= 4 the
# answer is 3.


def binary_search(T, p, r, k, x):
    if r >= p:
        mid = (p + r) // 2
        if T[mid] - k == x:
            return True
        elif T[mid] - k > x:
            return binary_search(T, p, mid - 1, k, x)
        else:
            return binary_search(T, mid + 1, r, k, x)
    return False


def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick_sort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quick_sort(T, p, q - 1)
        p = q + 1


def difference_by_k(T, k):
    quick_sort(T, 0, len(T) - 1)
    result = 0
    for i in range(0, len(T) - 1):
        if T[i] == T[i - 1]:
            continue
        elif binary_search(T, 0, len(T) - 1, k, T[i]):
            result += 1
    return result


k = 4
T = [7, 11, 3, 7, 3, 9, 5]
print(difference_by_k(T, k))
