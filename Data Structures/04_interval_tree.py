# Interval tree implementation
from math import inf


class Node:
    def __init__(self, root, key, l_span, r_span):
        self.key = key
        self.left = None
        self.right = None
        self.parent = root
        self.intervals = []
        self.left_span = l_span
        self.right_span = r_span


def add_interval(root, interval):
    if root.key is None:
        root.intervals.append(interval)
    elif root.key >= interval[1]:
        add_interval(root.left, interval)
    elif root.key <= interval[0]:
        add_interval(root.right, interval)
    elif interval[0] <= root.key <= interval[1]:
        if root.left_span >= interval[0] and root.right_span <= interval[1]:
            root.intervals.append(interval)
        else:
            add_interval(root.left, interval)
            add_interval(root.right, interval)


def point_intervals(root, point, result):
    while root is not None:
        for i in range(len(root.intervals)):
            result.append(root.intervals[i])
        if root.key is None or root.key == point:
            return result
        if point < root.key:
            root = root.left
        else:
            root = root.right


def create_interval_tree(T, root, a, b, l_span, r_span):
    if b < a:
        return Node(root, None, l_span, r_span)
    mid = (a + b) // 2
    new_node = Node(root, T[mid], l_span, r_span)
    if mid - a - 1 >= 0:
        new_node.left = create_interval_tree(T, new_node, a, mid - 1, new_node.left_span, new_node.key)
    else:
        new_node.left = Node(root, None, new_node.left_span, new_node.key)
    if b - mid - 1 >= 0:
        new_node.right = create_interval_tree(T, new_node, mid + 1, b, new_node.key, new_node.right_span)
    else:
        new_node.right = Node(root, None, new_node.key, new_node.right_span)
    return new_node


def print_tree(root):
    if root.left:
        print_tree(root.left)
    print(root.key, " -> SPAN: [", root.left_span, ", ", root.right_span, "]  ", sep="")
    if root.right:
        print_tree(root.right)


intervals = [[0, 10], [5, 20], [7, 12], [10, 15]]
T = []
for i in range(len(intervals)):
    T.append(intervals[i][0])
    T.append(intervals[i][1])
T.sort()
unique = [T[0]]
idx = 0
for i in range(1, len(T)):
    if T[i] != unique[idx]:
        unique.append(T[i])
        idx += 1
root = create_interval_tree(unique, None, 0, len(unique) - 1, -inf, inf)
add_interval(root, [5, 20])
add_interval(root, [7, 12])
print(point_intervals(root, 11, []))
print(point_intervals(root, 6, []))
print_tree(root)
