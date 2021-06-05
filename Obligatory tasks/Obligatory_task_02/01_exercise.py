# Proszę zaproponować jak najszybszy algorytm sortujący n elementową tablicę zawierająca liczby
# ze zbioru [0, 1, 2, ..., n^2-1].


def counting_sort(T, k):
    C = [0]*len(T)
    B = [0]*len(T)
    for i in range(len(T)):
        C[(T[i]//k) % len(T)] += 1
    for i in range(1, len(T)):
        C[i] += C[i-1]
    for i in range(len(T)-1, -1, -1):
        B[C[(T[i] // k) % len(T)]-1] = T[i]
        C[(T[i]//k) % len(T)] -= 1
    for i in range(len(T)):
        T[i] = B[i]


def radix_sort(T):
    counting_sort(T, 1)
    counting_sort(T, len(T))


T = [40, 112, 45, 32, 33, 1, 22, 111, 114, 17, 9]
radix_sort(T)
print(T)
