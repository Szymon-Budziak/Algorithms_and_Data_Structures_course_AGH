# Red-black tree implementation
class RBNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.color = 'BLACK'


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.root = self.nil


def rotate_left(T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.left = y
    y.left = x
    x.parent = y
    return


def rotate_right(T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.right = y
    y.right = x
    x.parent = y


def insert(T, value):
    z = RBNode(value)
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.value < x.value:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == T.nil:
        T.root = z
    elif z.value < y.value:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'RED'
    insert_fix_tree(T, z)


def insert_fix_tree(T, z):
    while z.parent.color == 'RED':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y is not None and y.color == 'RED':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    rotate_left(T, z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                rotate_right(T, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'RED':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    rotate_right(T, z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                rotate_left(T, z.parent.parent)
    T.root.color = 'BLACK'


T = RBTree()
insert(T, 10)
insert(T, 5)
insert(T, 20)
insert(T, 3)
insert(T, 25)
insert(T, 15)
insert(T, 12)
insert(T, 30)
