# We are given three strings A, B and C. A and B are of the same length. The following properties apply:
#   1) Letters at the sane index in strings A and B are equivalent
#   2) If letter a is equivalent with letter b, then letter b is equivalent with letter a
#   3) If letter a is equivalent with letter b and letter b is equivalent with letter c, then letter
#      a is equivalent to letter c
#   4) Each letter is equivalent to itself
# In string C we can replace any letter with a letter equivalent to it. What is the smallest
# lexicographically string that we can create in this way?


class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def make_set(val):
    return Node(val)


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def equivalent_letters(A, B, C):
    letters = []
    values = []
    for i in range(len(A)):
        if A[i] in values and B[i] in values:
            idx_x = values.index(A[i])
            x = letters[idx_x]
            idx_y = values.index(B[i])
            y = letters[idx_y]
        elif A[i] in values and B[i] not in values:
            y = make_set(B[i])
            letters.append(y)
            values.append(y.value)
            idx = values.index(A[i])
            x = letters[idx]
        elif B[i] in values and A[i] not in values:
            x = make_set(A[i])
            letters.append(x)
            values.append(x.value)
            idx = values.index(B[i])
            y = letters[idx]
        else:
            x = make_set(A[i])
            letters.append(x)
            values.append(x.value)
            y = make_set(B[i])
            letters.append(y)
            values.append(y.value)
        if A[i] > B[i]:
            union(x, y)
        else:
            union(y, x)
    word = list(C)
    for i in range(len(C)):
        if C[i] in values:
            idx = values.index(C[i])
            x = letters[idx]
            while x != x.parent:
                x = x.parent
            word[i] = x.value
    new_word = "".join(word)
    return new_word


A = "caef"
B = "fbga"
C = "abdfe"
print(equivalent_letters(A, B, C))
