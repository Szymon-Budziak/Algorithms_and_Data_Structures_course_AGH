# John worked all day and wrote down on a long paper strip his favorite number n consisting of l digits.
# Unfortunately, the strip turned out to be so long that it didn't fit in the John's bookshelf. To solve
# the issue, John decided to split the strip into two non-empty parts so that each of them contains
# a positive integer without leading zeros. After that he will compute the sum of the two integers
# and write it down on a new strip. John wants the resulting integer to be as small as possible, because
# it increases the chances that the sum will fit it in the bookshelf. Help John decide what is the
# minimum sum he can obtain.
from math import inf


def split_a_number(l, n):
    min_sum = inf
    T = [-1, 0, 1]
    for i in range(len(T)):
        mid = l // 2 + T[i]
        while 0 < mid < l and n[mid] == '0':
            if T[i] == -1:
                mid -= 1
            else:
                mid += 1
        if 0 < mid < l:
            min_sum = min(min_sum, int(n[mid:]) + int(n[:mid]))
    return min_sum


l = 20
n = '67378957561978988538'
print(split_a_number(l, n))
