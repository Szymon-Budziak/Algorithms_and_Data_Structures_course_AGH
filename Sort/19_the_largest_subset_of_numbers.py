# We are given an array A which has n natural numbers that take values in the range [0, ..., n]. Find
# algorithm that find the size of the largest subset of numbers from A such that their GCD is not 1.


def largest_subset_of_numbers(T):
    n = max(T)
    result = [0] * (n + 1)
    for i in range(len(T)):
        idx = 2
        while idx <= T[i]:
            if T[i] % idx == 0:
                result[idx] += 1
            idx += 1
    return max(result)


T = [1, 2, 4, 5, 1, 7, 8, 1, 3, 6, 8, 15, 27, 13, 11, 3, 9, 7, 2]
print(largest_subset_of_numbers(T))
