class RBNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.red = False


def fix_tree(root, node):
    while node != root and node.parent.red:
        if node.parent == node.parent.parent.right:
            uncle = node.parent.parent.left
            if uncle.red:
                uncle.red = False
                node.parent.red = False
                node.parent.parent.red = True
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    node = node.parent
                    root = rotate_right(root, node)
                node.parent.red = False
                node.parent.parent.red = True
                root = rotate_left(root, node.parent.parent)
        elif node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            if uncle.red:
                uncle.red = False
                node.parent.red = False
                node.parent.parent.red = True
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    node = node.parent
                    root = rotate_left(root, node)
                node.parent.red = False
                node.parent.parent.red = True
                root = rotate_right(root, node.parent.parent)
    root.red = False


def insert(root, value):
    new_node = RBNode(value)
    new_node.red = True
    parent = None
    current = root
    while current is not None:
        parent = current
        if new_node.value < current.value:
            current = current.left
        elif new_node.value > current.value:
            current = current.right
        else:
            return
    new_node.parent = parent
    if new_node.value < parent.value:
        parent.left = new_node
    else:
        parent.right = new_node
    fix_tree(root, new_node)
    return root


def rotate_left(root, node):
    right_node = node.right
    node.right = right_node.left
    if right_node.left is not None:
        right_node.left.parent = node
    right_node.parent = node.parent
    if node.parent is None:
        root = right_node
    elif node == node.parent.left:
        node.parent.left = right_node
    else:
        node.parent.right = right_node
    right_node.left = node
    node.parent = right_node
    return root


def rotate_right(root, node):
    left_node = node.left
    node.left = left_node.right
    if left_node.right is not None:
        left_node.right.parent = node
    left_node.parent = node.parent
    if node.parent is None:
        root = left_node
    elif node == node.parent.right:
        node.parent.right = left_node
    else:
        node.parent.left = left_node
    left_node.right = node
    node.parent = left_node
    return root


root = RBNode(10)
insert(root, 5)
insert(root, 20)
insert(root, 3)
insert(root, 25)
insert(root, 15)
insert(root, 12)
insert(root, 30)
