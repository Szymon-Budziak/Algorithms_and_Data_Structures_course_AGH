# Dany jest zbiór punktów X = {x 1 , . . . , x n } na prostej. Proszę podać algorytm,
# który znajduje minimalną liczbę przedziałów jednostkowych domkniętych, potrzebnych
# do pokrycia wszystkich punktów z X.

def cover_points(X):
    X.sort()
    max_right = count = 0
    for i in range(len(X)):
        if X[i] > max_right:
            max_right = X[i] + 1
            count += 1
    return count


X = [0.33, 2.1, 0.7, 10.2, 8.3, 7.1, 10, 3.3]
print(cover_points(X))
