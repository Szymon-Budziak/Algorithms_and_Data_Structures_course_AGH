# You have a permutation: an array a=[a[1] , a[2], ..., a[n]] of distinct integers from 1 to n.
# The length of the permutation n is odd. Consider the following algorithm of sorting the
# permutation in increasing order. A helper procedure of the algorithm, f(i), takes a single
# argument i (1 <= i <= n-1) and does the following. If a[i] > a[i+1], the values of a[i] and
# a[i+1] are exchanged. Otherwise, the permutation doesn't change. The algorithm consists of
# iterations, numbered with consecutive integers starting with 1. On the i-th iteration, the
# algorithm does the following:
#   - if i is odd, call f(1), f(3), ..., f(n-2),
#   - if i is even, call f(2), f(4), ..., f(n-1).
# It can be proven that after a finite number of iterations the permutation will be sorted in
# increasing order. After how many iterations will this happen for the first time?


def is_sorted_array(T):
    if all(T[i] <= T[i + 1] for i in range(len(T) - 1)):
        return True
    return False


def strange_sort(n, T):
    j = 0
    while j < n and not is_sorted_array(T):
        if j % 2 == 0:
            for k in range(0, n - 1, 2):
                if T[k] > T[k + 1]:
                    T[k], T[k + 1] = T[k + 1], T[k]
        else:
            for k in range(1, n, 2):
                if T[k] > T[k + 1]:
                    T[k], T[k + 1] = T[k + 1], T[k]
        j += 1
    return j


n = 9
T = [1, 2, 5, 8, 4, 7, 9, 6, 3]
print(strange_sort(n, T))
