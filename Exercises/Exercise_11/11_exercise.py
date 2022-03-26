# Dany jest ciąg klocków (K1, ..., Kn). Klocek K[i] zaczyna sie na pozycji a[i] i ciągnie się do pozycji
# b[i] (wszystkie pozycje to nieujemne liczby naturalne) oraz ma wysokość 1. Klocki układane są po
# kolei–jeśli klocek nachodzi na któryś z poprzednich, to jest przymocowywany na szczycie poprzedzajacego
# klocka). Na przykład dla klocków o pozycjach (1, 3), (2, 5), (0, 3), (8, 9), (4, 6) powstaje
# konstrukcja o wysokosci trzech klocków. Proszę podac możliwie jak najszybszy algorytm, który oblicza
# wysokość powstałej konstrukcji.


class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.height = 0
        self.left = None
        self.right = None
        self.parent = None


def place_a_brick(root, brick):
    while root is not None:
        if brick[0] > root.b or brick[1] < root.a:
            node = Node(brick[0], brick[1])
            root.left = node
            node.height = root.height + 1
            return
        elif root.right is not None:
            root.a = min(root.a, brick[0])
            root.b = max(root.b, brick[1])
            root = root.right
        else:
            node = Node(brick[0], brick[1])
            root.a = min(root.a, brick[0])
            root.b = min(root.b, brick[1])
            root.right = node
            node.height = root.height + 1
            return


def get_max_height(root, height):
    if root is None:
        return height
    height = max(height, root.height)
    return get_max_height(root.right, height) or get_max_height(root.left, height)


def height_of_bricks(bricks):
    root = Node(bricks[0][0], bricks[0][1])
    root.height = 1
    for i in range(1, len(bricks)):
        place_a_brick(root, bricks[i])
    height = get_max_height(root, 0)
    return height


bricks = [(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]
print(height_of_bricks(bricks))
