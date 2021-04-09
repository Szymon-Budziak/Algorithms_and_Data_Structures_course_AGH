# Tablica T jest długości n, ale zawiera tylko ceil(logn) różnych wartości. Proszę zaproponować
# jak najszybszy algorytm sortujący taką tablicę.


def counting_sort_letters(T, index):
    C = [0]*10
    B = [0]*len(T)
    for i in range(len(T)):
        idx = int(T[i][index])
        C[idx] += 1
    for i in range(1, 10):
        C[i] += C[i-1]
    for i in range(len(T)-1, -1, -1):
        idx = int(T[i][index])
        C[idx] -= 1
        B[C[idx]] = T[i]
    for i in range(len(T)):
        T[i] = B[i]


def radix_sort_letters(T, columns):
    for col in range(columns-1, -1, -1):
        counting_sort_letters(T, col)
    return T


def sort(T):
    max_length = 0
    for i in range(len(T)):
        T[i] = str(T[i])
        max_length = max(max_length, len(T[i]))
    for i in range(len(T)):
        if len(T[i]) < max_length:
            T[i] = "0"*(max_length-len(T[i])) + T[i]
    radix_sort_letters(T, max_length)
    for i in range(len(T)):
        T[i] = int(T[i])


T = [365, 45137, 12, 45137, 12, 12, 45137, 365, 12]
sort(T)
print(T)
