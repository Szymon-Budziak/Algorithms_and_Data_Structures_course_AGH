# Zbiór przedziałów [(a[1], b[1]), ..., (a[n], b[n])], każdy przedział należy do [0, 1]. Opisać algorytm
# który sprawdzi czy jest możliwy taki wybór przedziałów, aby cały przedział [0, 1] zawierał się
# w wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.


def minimum_intervals(T):
    T.sort(key=lambda x: x[0])
    i = 0
    end = 0
    result = []
    while i < len(T) and end != 1:
        actual_start = T[i][0]
        actual_end = T[i][1]
        flag = True
        while i != len(T) and T[i][0] <= end:
            if actual_end < T[i][1]:
                actual_start = T[i][0]
                actual_end = T[i][1]
            i += 1
            flag = False
        if flag:
            i += 1
        result.append((actual_start, actual_end))
        end = actual_end
    return result


T = [[0, 0.4], [0, 0.35], [0.2, 0.6], [0.4, 0.6], [0.5, 0.6], [0.1, 0.9], [0.85, 1], [0.9, 1],
     [0.3, 0.4], [0.35, 0.4], [0.2, 0.75], [0.4, 1], [0.55, 1], [0.6, 1], [0.9, 1]]
print(minimum_intervals(T))
