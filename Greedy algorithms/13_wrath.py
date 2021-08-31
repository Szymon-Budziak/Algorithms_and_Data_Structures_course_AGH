# There are n guilty people in a line, the i-th of them holds a claw with length L[i]. The bell rings
# and every person kills some of people in front of him. All people kill others at the same time.
# Namely, the i-th person kills the j-th person if and only if j < i and j >= i-L[i]. We are given
# lengths of the claws. We need to find the total number of alive people after the bell rings.


def wrath(L):
    T = [0] * (len(L) + 10)
    for i in range(len(L)):
        T[max(0, i - L[i])] += 1
        T[i] -= 1
    result = len(L)
    for i in range(len(L)):
        T[i] += T[i - 1]
        if T[i] > 0:
            result -= 1
    return result


L = [1, 0, 0, 1, 1, 3, 2, 0, 0, 2, 3]
print(wrath(L))
