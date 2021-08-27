# B-tree implementation


class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t


def btree_search(T, k, x=None):
    if x is not None:
        i = 0
        while i < len(x.keys) and k > x.keys[i][0]:
            i += 1
        if i < len(x.keys) and k == x.keys[i][0]:
            return (x, i)
        elif x.leaf:
            return None
        else:
            return btree_search(T, k, x.child[i])
    else:
        return btree_search(T, k, T.root)


def btree_split_child(T, x, i):
    y = x.child[i]
    z = BTreeNode(y.leaf)
    x.child.insert(i + 1, z)
    x.keys.insert(i, y.keys[T.t - 1])
    z.keys = y.keys[T.t: (2 * T.t) - 1]
    y.keys = y.keys[0: (T.t - 1)]
    if not y.leaf:
        z.child = y.child[T.t:2 * T.t]
        y.child = y.child[0:T.t - 1]


def btree_insert_(T, k):
    root = T.root
    if len(root.keys) == (2 * T.t) - 1:
        current = BTreeNode()
        T.root = current
        current.child.insert(0, root)
        btree_split_child(T, current, 0)
        btree_insert_nonfull(T, current, k)
    else:
        btree_insert_nonfull(T, root, k)


def btree_insert_nonfull(T, x, k):
    i = len(x.keys) - 1
    if x.leaf:
        x.keys.append((0, 0))
        while i >= 0 and k[0] < x.keys[i][0]:
            x.keys[i + 1] = x.keys[i]
            i -= 1
        x.keys[i + 1] = k
    else:
        while i >= 0 and k[0] < x.keys[i][0]:
            i -= 1
        i += 1
        if len(x.child[i].keys) == (2 * T.t) - 1:
            btree_split_child(T, x, i)
            if k[0] > x.keys[i][0]:
                i += 1
        btree_insert_nonfull(T, x.child[i], k)


def print_btree(T, x, length):
    print("Level", length, end=" ")
    for i in x.keys:
        print(i, end=" ")
    print()
    length += 1
    if len(x.child) > 0:
        for i in x.child:
            print_btree(T, i, length)


Btree = BTree(4)
for i in range(15):
    btree_insert_(Btree, (i, 2 * i))
print_btree(Btree, Btree.root, 0)
print(btree_search(Btree, 12))
print(btree_search(Btree, 39))
