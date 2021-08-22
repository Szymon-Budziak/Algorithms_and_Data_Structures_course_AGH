# Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który znajduje
# takie dwie liczby x i y z A, że y − x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
# że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i + 1]
# dla których A[i + 1] − A[i] jest największe).


def max_span(T):
    minimum = maximum = T[0]
    for i in range(1, len(T)):
        maximum = max(maximum, T[i])
        minimum = min(minimum, T[i])
    A = [[] for _ in range(len(T))]
    x = (maximum + minimum) / len(T)
    for i in range(len(T)):
        bucket_num = int((T[i] - minimum) / x)
        A[bucket_num].append(T[i])
    result = 0
    prev_maximum = max(A[0])
    best_numbers = 0
    for i in range(1, len(T)):
        if len(A[i]) == 0:
            continue
        else:
            actual_minimum = min(A[i])
            if actual_minimum - prev_maximum > result:
                best_numbers = (actual_minimum, prev_maximum)
                result = actual_minimum - prev_maximum
            prev_maximum = max(A[i])
    return result, best_numbers


T = [0.5, 0.3, 0.01, 0.7, 0.2, 0.92, 0.11, 0.91]
print(max_span(T))
