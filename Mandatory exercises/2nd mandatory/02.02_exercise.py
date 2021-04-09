# Tablica T jest długości n, ale zawiera tylko ceil(logn) różnych wartości. Proszę zaproponować
# jak najszybszy algorytm sortujący taką tablicę.


def counting_sort(T, k):
    C = [0]*len(T)
    B = [0]*10
    for i in range(len(T)):
        index = T[i]/k
        B[int(index % 10)] += 1
    for i in range(1, 10):
        B[i] += B[i-1]
    j = len(T)-1
    while j >= 0:
        index = T[j]/k
        C[B[int(index % 10)]-1] = T[j]
        B[int(index % 10)] -= 1
        j -= 1
    for i in range(len(T)):
        T[i] = C[i]


def radix_sort(T):
    maximum = 0
    for i in range(len(T)):
        maximum = max(maximum, T[i])
    i = 1
    while maximum/i > 0:
        counting_sort(T, i)
        i *= 10


def digits(number):
    length = 0
    while number > 0:
        length += 1
        number //= 10
    return length


def sort(T):
    max_length = 0
    for i in range(len(T)):
        max_length = max(max_length, digits(T[i]))
    for i in range(len(T)):
        T[i] += (10**max_length)
    radix_sort(T)
    for i in range(len(T)):
        T[i] -= (10**max_length)


T = [365, 45137, 12, 45137, 12, 12, 45137, 365, 12]
sort(T)
print(T)
