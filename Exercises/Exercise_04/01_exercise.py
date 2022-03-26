# Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb
# ze zbioru 0, ..., n**2−1.


def counting_sort(T, f):
    count = [0] * len(T)
    result = [0] * len(T)
    for i in range(len(T)):
        count[f(T[i])] += 1
    for i in range(1, len(T)):
        count[i] += count[i - 1]
    for i in range(len(T) - 1, -1, -1):
        count[f(T[i])] -= 1
        result[count[f(T[i])]] = T[i]
    for i in range(len(T)):
        T[i] = result[i]


def sort_nsq(T):
    counting_sort(T, lambda x: x % len(T))
    counting_sort(T, lambda x: x // len(T))
    return T


n = 15
T = [187, 115, 185, 129, 139, 223, 36, 177, 28, 71, 84, 101, 168, 70, 189]
print(sort_nsq(T))
