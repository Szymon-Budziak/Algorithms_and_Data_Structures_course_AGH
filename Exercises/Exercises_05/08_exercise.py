# Dana jest szachownica A o wymiarach n×n. Szachownica zawiera liczby wymierne. Należy przejść
# z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół” oraz “w prawo”. Wejście na dane pole
# kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm znajdujący trasę o minimalnym koszcie.


def traverse_chessboard(A, rows, cols):
    T = [[0] * cols for _ in range(rows)]
    T[0][0] = A[0][0]
    for i in range(1, cols):
        T[0][i] = T[0][i - 1] + A[0][i]
    for i in range(1, rows):
        T[i][0] = T[i - 1][0] + A[i][0]
    for i in range(1, rows):
        for j in range(1, cols):
            T[i][j] = min(T[i][j - 1], T[i - 1][j]) + A[i][j]
    i = j = 0
    print(T[i][j], end=" -> ")
    while i != rows - 1 and j != cols - 1:
        if T[i][j + 1] < T[i + 1][j]:
            print(A[i][j + 1], end=" -> ")
            j += 1
        else:
            print(A[i + 1][j], end=" -> ")
            i += 1
    if i == rows - 1 or j == cols - 1:
        print(A[-1][-1])
    return T[-1][-1]


A = [[1, 3, 5, 8],
     [4, 2, 1, 7],
     [4, 3, 2, 3]]
rows = len(A)
cols = len(A[0])
print(traverse_chessboard(A, rows, cols))
