# Given a rod of length n inches and a table of prices T[i] for i = [1, 2, ..., n].
# Determine the maximum revenue r[n] obtainable by cutting up the rod and selling
# the pieces.
from time import perf_counter


# 1st solution: Top-down with memoization


def memoized_cut_rod(T, n):
    revenue = [-1]*(n+1)
    return memoized_cut_rod_aux(T, revenue, n)


def memoized_cut_rod_aux(T, revenue, n):
    if revenue[n-1] > 0:
        return revenue[n-1]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(0, n):
            q = max(q, T[i]+memoized_cut_rod_aux(T, revenue, n-i-1))
    revenue[n-1] = q
    return q


# 2nd solution: bottom-up method


def bottom_up_cut_rod(T, n):
    revenue = [-1]*(n+1)
    revenue[0] = 0
    for i in range(1, n+1):
        q = -1
        for j in range(i):
            q = max(q, T[j]+revenue[i-j-1])
        revenue[i] = q
    return revenue[n]


# 3rd solution: extended bottom-up method to show optimal cut

def extended_bottom_up_cut_rod(T, n):
    revenue = [-1]*(n+1)
    size = [0]*(n+1)
    revenue[0] = 0
    for i in range(1, n+1):
        q = -1
        for j in range(i):
            if q < T[j]+revenue[i-j-1]:
                q = T[j]+revenue[i-j-1]
                size[i] = j+1
        revenue[i] = q
    return (revenue, size, q)


def print_cut_rod_solution(T, n):
    r, s, q = extended_bottom_up_cut_rod(T, n)
    print(q, end=' (')
    while n > 0:
        print(s[n], end=', ')
        n = n - s[n]
    print(')')


T = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 34, 34, 30, 49, 45, 43, 43, 52, 52]
n = 15

start1 = perf_counter()
print(memoized_cut_rod(T, n))
end1 = perf_counter()

start2 = perf_counter()
print(bottom_up_cut_rod(T, n))
end2 = perf_counter()

start3 = perf_counter()
print_cut_rod_solution(T, n)
end3 = perf_counter()

print('1st:', end1-start1)
print('2nd:', end2-start2)
print('3rd:', end3-start3)
