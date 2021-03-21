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


T = [349, 12, 12, 283, 349, 283, 283, 12]
radix_sort(T)
print(T)
