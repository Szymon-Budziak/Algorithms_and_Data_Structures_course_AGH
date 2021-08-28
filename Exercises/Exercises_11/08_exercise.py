# Rozważmy drzewa BST, które dodatkowo w każdym węźle zawierają pole z liczbą węzłów w danym
# poddrzewie. Proszę opisać jak w takim drzewie wykonywać następujące operacje:
#   1) znalezienie i-go co do wielkości elementu,
#   2) wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł.
# Proszę zaimplementować obie operacje.


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.left_size = 0
        self.right_size = 0


def insert(root, key, value):
    previous = None
    while root is not None:
        if key > root.key:
            previous = root
            root.right_size += 1
            root = root.right
        else:
            previous = root
            root.left_size += 1
            root = root.left
    node = BSTNode(key, value)
    if key > previous.key:
        previous.right = node
        node.parent = previous
    else:
        previous.left = node
        node.parent = previous


def find_ith_element(root, i):
    while root is not None:
        if i == root.left_size + 1:
            return root.key
        elif i <= root.left_size:
            root = root.left
        else:
            i -= (root.left_size + 1)
            root = root.right
    return None


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def get_size(root, key):
    node = find(root, key)
    count = node.left_size + 1
    while node.parent is not None:
        if node.parent.right is not None and node.parent.right == node:
            count += (node.parent.left_size + 1)
        node = node.parent
    return count


root = BSTNode(2, 7)
insert(root, 8, 7)
insert(root, 1, 7)
insert(root, 19, 7)
insert(root, 23, 7)
insert(root, 14, 7)
insert(root, 5, 7)
print(find_ith_element(root, 2))
print(find_ith_element(root, 25))
print(get_size(root, 19))
print(get_size(root, 5))
