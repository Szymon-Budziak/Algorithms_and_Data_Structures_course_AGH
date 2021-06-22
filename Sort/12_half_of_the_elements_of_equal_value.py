# We are given an array A with a natural numbers. Find algorithm with O(n) complexity which determines
# whether more than half of the elements int the array have the same value.


# 1st solution:


def insertion_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


def half(A):
    maximum = max(A) + 1
    buckets = [[] for _ in range(len(A))]
    for i in range(len(A)):
        index = int((A[i] / maximum) * len(A))
        buckets[index].append(A[i])
    for i in range(len(buckets)):
        if len(buckets[i]) > len(A) // 2:
            insertion_sort(buckets[i])
            count = best_count = 1
            actual = buckets[i][0]
            for j in range(1, len(buckets[i])):
                if buckets[i][j] == actual:
                    count += 1
                else:
                    actual = buckets[i][j]
                    count = 1
                best_count = max(best_count, count)
            if best_count > len(A) // 2:
                return True
    return False


# 2nd solution:


def half2(A):
    maximum = max(A)
    buckets = [[] for _ in range(len(A) + 1)]
    for i in range(len(buckets)):
        buckets[i].append(0)
    for i in range(len(A)):
        index = int((A[i] / maximum) * len(A))
        buckets[index].append(A[i])
        buckets[index][0] += 1
        if buckets[index][0] > len(A) // 2:
            return True
    return False


A = [12, 3, 5, 7, 7, 12, 7, 4, 10, 2, 7, 7, 7, 7, 7]
print(half(A))
print(half2(A))
