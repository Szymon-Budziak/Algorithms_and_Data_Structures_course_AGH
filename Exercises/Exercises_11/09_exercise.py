# Proszę zapropnować algorytm, który oblicza sumę wszystkich wartości w drzewie binarnym zdefiniowanym
# na węzłach typu:
# class BNode:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.value = value
# Program może korzystać wyłącznie ze stałej liczby zmiennych (ale wolno mu zmieniać strukturę drzewa,
# pod warunkiem, że po zakończonych obliczeniach drzewo zostanie przywrócone do stanu początkowego.)


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def insert(root, value):
    previous = None
    while root is not None:
        if root.value > value:
            previous = root
            root = root.left
        else:
            previous = root
            root = root.right
    if value < previous.value:
        previous.left = BNode(value)
        previous.left.parent = previous
    else:
        previous.right = BNode(value)
        previous.right.parent = previous


def sum_values(root, summary):
    if root is None:
        return summary
    root.value += sum_values(root.right, summary)
    summary = root.value
    return sum_values(root.left, summary)


root = BNode(12)
insert(root, 46)
insert(root, 54)
insert(root, 4)
insert(root, 23)
insert(root, 11)
insert(root, 39)
insert(root, 26)
print(sum_values(root, 0))
