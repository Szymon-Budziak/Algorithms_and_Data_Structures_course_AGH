# We are given an array a of length n consisting of integers. We can apply the following operation,
# consisting of several steps, on the array a zero or more times:
# - we select two different numbers in the array a[i] and a[j],
# - we remove i-th and j-th elements from the array.
# For example, if n=6 and a=[1, 6, 1, 1, 4, 4], then you can perform the following sequence of operations:
# - select i=1,j=5. The array a becomes equal to [6, 1, 1, 4],
# - select i=1,j=2. The array a becomes equal to [1, 4].
# What can be the minimum size of the array after applying some sequence of operations to it?


def epic_transformation(T, n):
    count = []
    for j in range(len(T)):
        if T[j] not in count:
            count.append([T[j], 0])
    for j in range(len(T)):
        for k in range(len(count)):
            if T[j] == count[k][0]:
                count[k][1] += 1
    max_amount = 0
    for j in range(len(count)):
        max_amount = max(max_amount, count[j][1])
    if max_amount > n - max_amount:
        return max_amount - (n - max_amount)
    else:
        return n % 2


T = [6, 6, 4, 2, 4, 6, 2, 2, 2, 4, 6, 4]
print(epic_transformation(T, len(T)))
