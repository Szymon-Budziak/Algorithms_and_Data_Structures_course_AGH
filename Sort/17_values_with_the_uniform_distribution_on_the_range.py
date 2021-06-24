# We are given a class:
# class Node:
#   def __init__(self):
#       val = 0
#       next = None
# that represents a node in a one-direction cross reference chain, in which val values of individual
# nodes were generated according to a uniform distribution on the range [a, b]. Find algorithm
# sort(first) that sorts such an array.


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def insertion_sort(T):
    for i in range(len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j].value > key.value:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def sort(first):
    count = 0
    head = first
    max_value = 0
    while head is not None:
        count += 1
        max_value = max(max_value, head.value)
        head = head.next
    bucket = [[] for _ in range(count + 1)]
    while first is not None:
        index = int((first.value / max_value) * count)
        bucket[index].append(first)
        first = first.next
    for i in range(len(bucket)):
        insertion_sort(bucket[i])
    result = [0] * count
    idx = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            result[idx] = bucket[i][j].value
            idx += 1
    return result


def make_linked_list(l):
    n = len(l)
    p = None
    for i in range(n - 1, -1, -1):
        q = Node()
        q.value = l[i]
        q.next = p
        p = q
    return p


T = [6, 2, 11, 6, 10, 13, 9, 11, 4, 3, 15, 3, 1, 13, 1, 9, 1, 14, 11, 7, 8, 6, 12, 5, 10, 8, 2, 7, 4, 12]
linked_list = make_linked_list(T)
print(sort(linked_list))
