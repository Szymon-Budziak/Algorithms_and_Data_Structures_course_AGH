# class field:
#     def __init__(self, value, long_j, short_j):
#         self.value = value
#         self.long_j = long_j
#         self.short_j = short_j
# Z każdego pola można skakać tylko o ilość pól zapisaną w long_j lub short_j. Napisać program który
# zwróci maksymalną wartość jaką możemy osiągnąć poprzez przejście z pola 0 do n-1. Można założyć,
# że z każdego pola da się dojść do pola n-1.
from random import randint


class field:
    def __init__(self, value, long_j, short_j):
        self.value = value
        self.long_j = long_j
        self.short_j = short_j


def maximum_transition_value(T):
    DP = [0] * len(T)
    DP[len(T) - 1] = T[len(T) - 1].value
    for i in range(len(T) - 2, -1, -1):
        if T[i].short_j + i < len(T):
            DP[i] = DP[T[i].short_j + i] + T[i].value
        if T[i].long_j + i < len(T):
            DP[i] = max(DP[i], DP[T[i].long_j + i] + T[i].value)
    return DP[0]


values = [(10, 3, 2), (2, 4, 1), (5, 5, 1), (10, 3, 2), (10, 5, 1),
          (2, 4, 2), (9, 4, 1), (2, 3, 2), (10, 5, 1), (2, 5, 1)]
T = []
for i in range(len(values)):
    T.append(field(values[i][0], values[i][1], values[i][2]))
print(maximum_transition_value(T))
