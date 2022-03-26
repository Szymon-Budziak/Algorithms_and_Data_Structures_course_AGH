# Dane jest drzewo ukorzenione T, gdzie każdy wierzchołek v ma - potencjalnie ujemną — wartość value(v).
# Proszę zaproponować algorytm, który znajduje wartość najbardziej wartościowej ścieżki w drzewie T.


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.path = 0


def the_most_valuable_path(v):
    if v is None:
        return 0, 0
    left_node, left_path = the_most_valuable_path(v.left)
    right_node, right_path = the_most_valuable_path(v.right)
    v.path = max(0, v.value, v.value + left_node, v.value + right_node)
    best_path = max(v.path, left_path, right_path)
    return v.path, best_path


root = Node(-5)
a = Node(3)
b = Node(2)
c = Node(7)
d = Node(4)
e = Node(2)
f = Node(13)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
print(the_most_valuable_path(root)[1])
