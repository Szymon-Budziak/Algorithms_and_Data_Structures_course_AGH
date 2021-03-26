# A - tablica zawierająca na parami różnych liczb (nieposortowana)
# Proszę znaleźć liczby A[i], A[j] takie, że:
#   a) A[i] - A[j] jest największe
#   b) nie ma liczby A[t]: A[i] > A[t] > A[j]


def max_span(T):
    minimum = maximum = T[0]
    for i in range(1, len(T)):
        maximum = max(maximum, T[i])
        minimum = min(minimum, T[i])
    A = [[] for _ in range(len(T))]
    x = (maximum+minimum)/len(T)
    for i in range(len(T)):
        bucket_num = int((T[i] - minimum)/x)
        A[bucket_num].append(T[i])
    result = 0
    prev_maximum = max(A[0])
    for i in range(1, len(T)):
        if len(A[i]) == 0:
            continue
        else:
            actual_minimum = min(A[i])
            result = max(result, actual_minimum - prev_maximum)
            prev_maximum = max(A[i])
    return result


T = [0.5, 0.3, 0.01, 0.7, 0.2, 0.92, 0.11, 0.91]
print(max_span(T))
