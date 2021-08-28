# W pewnym laboratorium genetycznym powstał ciąg sekwencji DNA. Każda sekwencja to pewien napis
# składający się z symboli G, A, T i C. Przed dalszymi badaniami konieczne jest upewnić się, że wszystkie
# sekwencje DNA są parami rózne. Proszę opisać algorytm, który sprawdza czy tak faktycznie jest.


# 1st solution using tree:


class Node:
    def __init__(self):
        self.G = None
        self.A = None
        self.T = None
        self.C = None
        self.end = False


def check_DNA(root, sequence, idx):
    if idx == len(sequence):
        if root.end:
            return False
        root.end = True
        return True
    if sequence[idx] == 'G':
        if root.G is None:
            root.G = Node()
        return check_DNA(root.G, sequence, idx + 1)
    elif sequence[idx] == 'A':
        if root.A is None:
            root.A = Node()
        return check_DNA(root.A, sequence, idx + 1)
    elif sequence[idx] == 'T':
        if root.T is None:
            root.T = Node()
        return check_DNA(root.T, sequence, idx + 1)
    else:
        if root.C is None:
            root.C = Node()
        return check_DNA(root.C, sequence, idx + 1)


def different_sequences_tree(sequence):
    root = Node()
    for i in range(len(sequence)):
        if not check_DNA(root, sequence[i], 0):
            return False
    return True


# 2nd solution using sort:


def counting_sort(sequence, i):
    count = [0] * (ord('Z') - ord('A') + 1)
    result = [0] * len(sequence)
    for j in range(len(sequence)):
        count[ord(sequence[j][i]) - ord('A')] += 1
    for j in range(1, len(count)):
        count[j] += count[j - 1]
    for j in range(len(sequence) - 1, -1, -1):
        index = ord(sequence[j][i]) - ord('A')
        result[count[index] - 1] = sequence[j]
        count[index] -= 1
    for j in range(len(sequence)):
        sequence[j] = result[j]


def radix_sort(sequence):
    for i in range(len(sequence[0]) - 1, -1, -1):
        counting_sort(sequence, i)


def different_sequences_sort(sequence):
    for i in range(len(sequence)):
        sequence[i] = (len(sequence[i]), sequence[i])
    maximum = 0
    for i in range(len(sequence)):
        maximum = max(maximum, sequence[i][0])
    buckets = [[] for _ in range(maximum + 1)]
    for i in range(len(sequence)):
        buckets[sequence[i][0]].append(sequence[i][1])
    for i in range(len(buckets)):
        if len(buckets[i]) != 0:
            radix_sort(buckets[i])
    result = []
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            result.append(buckets[i][j])
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            return False
    return True


sequence = ["ATC", "GA", "GAGTC", "TTCAC", "TCG", "GA", "TTG"]
print(different_sequences_tree(sequence))
print(different_sequences_sort(sequence))
