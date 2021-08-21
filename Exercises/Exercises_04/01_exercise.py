# Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb
# ze zbioru 0, ..., n**2−1.


def countsort(T, f):
    B = [0] * len(T)
    C = [0] * len(T)
    for i in range(len(T)):
        C[f(T[i])] += 1
    for i in range(1, len(T)):
        C[i] += C[i - 1]
    for i in range(len(T) - 1, -1, -1):
        C[f(T[i])] -= 1
        B[C[f(T[i])]] = T[i]
    for i in range(len(T)):
        T[i] = B[i]


def sort_nsq(T):
    countsort(T, lambda x: x % len(T))
    countsort(T, lambda x: x // len(T))
    return T


n = 15
T = [187, 115, 185, 129, 139, 223, 36, 177, 28, 71, 84, 101, 168, 70, 189]
print(sort_nsq(T))
