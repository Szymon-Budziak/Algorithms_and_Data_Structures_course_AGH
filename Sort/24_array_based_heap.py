# We are given an array of real numbers of size n that is represented as minimum heap (array-based
# heap). Having given the real number x, check if the k-th smallest element is greater than or
# equal to x.


def right_child(index):
    return 2 * index + 1


def left_child(index):
    return 2 * index + 2


def parent(index):
    return (index - 1) // 2


def min_heap(T, x, index=0, k=0):
    if x <= T[0]:
        return False
    if T[index] < x:
        k += 1
    else:
        return k
    left = left_child(index)
    if left < len(T):
        k = min_heap(T, x, left, k)
    right = right_child(index)
    if right < len(T):
        k = min_heap(T, x, right, k)
    return k


T = [2, 4, 5, 7, 9, 6, 12, 11, 14, 13, 8, 15, 16]
x = 10
print(min_heap(T, x))
