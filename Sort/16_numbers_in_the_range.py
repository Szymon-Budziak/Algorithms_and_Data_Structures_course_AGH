# We are given an array with n numbers from the range [0, ..., n^2-1]. Find algorithm that sorts such
# an array in O(n) time.


def counting_sort(T, func):
    count = [0] * len(T)
    result = [0] * len(T)
    for i in range(len(T)):
        count[func(T[i])] += 1
    for i in range(1, len(T)):
        count[i] += count[i - 1]
    for i in range(len(T) - 1, -1, -1):
        count[func(T[i])] -= 1
        result[count[func(T[i])]] = T[i]
    for i in range(len(T)):
        T[i] = result[i]


def numbers_in_the_range(T):
    counting_sort(T, lambda x: x % len(T))
    counting_sort(T, lambda x: x // len(T))
    return T


T = [35, 9, 40, 12, 64, 27, 20, 92, 16, 46]
print(numbers_in_the_range(T))
