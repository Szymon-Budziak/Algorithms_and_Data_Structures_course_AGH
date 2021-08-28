# Little Vasya has received a young builder’s kit. The kit consists of several wooden bars, the lengths
# of all of them are known. The bars can be put one on the top of the other if their lengths are the same.
# Vasya wants to construct the minimal number of towers from the bars. Help Vasya to use the bars in the
# best way possible.
# We are given a list of integers (1<= N <= 1000) — the lengths of the bars. All the lengths are natural
# numbers not exceeding 1000. Find the height of the largest tower and their total number. Remember that
# Vasya should use all the bars.


def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q - p <= r - q:
            quicksort(T, p, q - 1)
            p = q + 1
        else:
            quicksort(T, q, r)
            r = q - 1


def towers(T):
    quicksort(T, 0, len(T) - 1)
    previous = T[0]
    count = 1
    max_height = actual_height = 1
    for i in range(1, len(T)):
        if T[i] == previous:
            actual_height += 1
            max_height = max(max_height, actual_height)
        else:
            previous = T[i]
            actual_height = 1
            count += 1
    return (max_height, count)


T = [1, 8, 2, 3, 9, 3, 15, 15, 3]
print(towers(T))
