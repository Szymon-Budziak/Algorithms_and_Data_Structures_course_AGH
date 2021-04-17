# Given a positive number n. Count all possible distinct binary strings (0/1)
# of length n that there are not consecutive 1's.


def count_binary_strings(n):
    A = [0]*n
    B = [0]*n
    A[0] = B[0] = 1
    for i in range(1, n):
        A[i] = A[i-1] + B[i-1]
        B[i] = A[i-1]
    return A[n-1]+B[n-1]


n = 4
print(count_binary_strings(n))
