class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def insert(root, key):
    previous = None
    while root is not None:
        if root.key > key:
            previous = root
            root = root.left
        else:
            previous = root
            root = root.right
    if previous.key == key:
        return False
    elif previous.parent is not None and previous.parent.key == key:
        return False
    elif previous.left is not None and previous.left.key == key:
        return False
    elif previous.right is not None and previous.right.key == key:
        return False
    if key < previous.key:
        previous.left = BSTNode(key)
        previous.left.parent = previous
        return True
    elif key > previous.key:
        previous.right = BSTNode(key)
        previous.right.parent = previous
        return True


def minimum(root):
    while root.left is not None:
        root = root.left
    return root.key


def successor(root, actual_root_value):
    actual_root = find(root, actual_root_value)
    value = actual_root.key
    if actual_root.right is not None:
        return minimum(actual_root.right)
    while actual_root.parent is not None and actual_root.parent.key < actual_root.key:
        actual_root = actual_root.parent
    if actual_root.parent is not None:
        if actual_root.parent.key < value:
            return None
        return actual_root.parent.key
    if actual_root.key < value:
        return None


def remove(root, key):
    actual_root = find(root, key)
    if actual_root is None:
        return False
    elif actual_root.right is None:
        if actual_root.left is None:
            if actual_root.parent.left is not None and actual_root.parent.left.key == actual_root.key:
                actual_root.parent.left = None
                return True
            else:
                actual_root.parent.right = None
                return True
        else:
            if actual_root.parent.left is not None and actual_root.parent.left.key == actual_root.key:
                actual_root.parent.left = actual_root.left
                return True
            elif actual_root.parent.right is not None and actual_root.parent.right.key == actual_root.key:
                actual_root.parent.right = actual_root.right
                return True
    elif actual_root.left is None:
        if actual_root.parent.left is not None and actual_root.parent.left.key == actual_root.key:
            actual_root.parent.left = actual_root.right
            return True
        if actual_root.parent.right is not None and actual_root.parent.right.key == actual_root.key:
            actual_root.parent.right = actual_root.right
            return True
    else:
        root_value = successor(root, actual_root.key)
        remove(root, root_value)
        actual_root.key = root_value
        return True


root = BSTNode(20)
print(insert(root, 10))
print(insert(root, 27))
print(insert(root, 5))
print(remove(root, 100))
print(insert(root, 15))
print(insert(root, 28))
print(insert(root, 30))
print(remove(root, 30))
print(insert(root, 35))
print(insert(root, 28))
print(insert(root, 40))
print(insert(root, 40))
print(remove(root, 20))
print(remove(root, 40))
print(remove(root, 13))
print(remove(root, 400))
print(remove(root, 30))
