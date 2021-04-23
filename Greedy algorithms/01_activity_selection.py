# Given n activities with their start and finish time (start, finish). Find
# set that has maximum number of non-conflicting activities that can be executed
# in a single time frame.


def activity_selection(T):
    T.sort(key=lambda x: x[1])
    A = []
    A.append(T[0])
    index = 0
    for i in range(1, len(T)):
        if T[i][0] >= A[index][1]:
            A.append(T[i])
            index += 1
    return A


T = [(8, 12), (6, 10), (8, 11), (5, 7), (12, 16), (5, 9),
     (3, 5), (0, 6), (1, 4), (2, 14), (3, 9)]
print(activity_selection(T))
