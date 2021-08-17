# Proszę podać algorytm, który mając na wejściu drzewo oblicza skojarzenie o maksymalnej liczności.
# Czy algorytm dalej będzie działać jeśli każda krawędź będzie mieć dodatnią wagę i szukamy
# skojarzenia o maksymalnej sumie wag?


class BST_node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.with_root = 0
        self.without_root = 0


def insert(root, key):
    previous = None
    while root is not None:
        if root.key > key:
            previous = root
            root = root.left
        else:
            previous = root
            root = root.right
    if key < previous.key:
        previous.left = BST_node(key)
        previous.left.parent = previous
    else:
        previous.right = BST_node(key)
        previous.right.parent = previous


def create_tree(values):
    root = BST_node(values[0])
    for i in range(1, len(values)):
        insert(root, values[i])
    return root


def max_matching(root):
    if root.left is not None and root.right is not None:
        max_matching(root.left)
        max_matching(root.right)
        root.without_root = max(root.without_root, root.left.with_root + root.right.with_root)
        root.with_root = max(root.with_root, root.left.with_root + root.right.without_root + 1,
                             root.left.without_root + root.right.with_root + 1, root.without_root)
    elif root.right is not None:
        max_matching(root.right)
        root.with_root = max(root.with_root, root.right.with_root, root.right.without_root + 1)
        root.without_root = max(root.without_root, root.right.with_root)
    elif root.left is not None:
        max_matching(root.left)
        root.with_root = max(root.with_root, root.left.with_root, root.left.without_root + 1)
        root.without_root = max(root.without_root, root.left.with_root)
    return root.with_root


values = [14, 5, 17, 19, 2, 59, 6, 94, 11]
tree = create_tree(values)
print(max_matching(tree))
